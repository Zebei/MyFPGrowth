# -*- coding: UTF8 -*-
from fp_tree import test_fp_tree, node, fp_tree
from csv_to_dataset import csv_to_dataset
import itertools #用于生成排列组合的link

#首先，对tree_form 进行排序
def tree_form_sorted(tree_from):

    num_tree_form = {}
    for key in tree_form:
        num_tree_form[key] = tree_form[key][0]
    #将tree_form 的排序元素提取出来

    sorted_tree_form = sorted(num_tree_form.items(), key = lambda asd:asd[1], reverse=False)
    return sorted_tree_form


#找出元素item在sorteditem中的次序
def num_of_sorteditem(item):

    global sorteditem

    for i in range(len(sorteditem) - 1):
        if sorteditem[i][0] == item:
            return i


#删除trans中所有排在node之后的元素，并且将trans递减排序
def fp_base_pre(trans, this_node):

    global sorteditem
    new_trans = []

    for item in trans:
        if num_of_sorteditem(item) > num_of_sorteditem(this_node):
            new_trans.append(item)

    #找出trans中序号大于node的元素，保存在new_trans中

    len_new_trans = len(new_trans)
    sorted_new_trans = [0] * (len_new_trans)
    max_node = this_node

    #注意项集可能为空
    for i in range(len_new_trans):
        max_node = this_node
        for item in new_trans:
            if num_of_sorteditem(item) > num_of_sorteditem(max_node):
                max_node = item

        sorted_new_trans[i] = max_node

        del new_trans[new_trans.index(max_node)]
        #排序

    if sorted_new_trans != []:
        return sorted_new_trans
    else:
        return []


#找出节点的条件模式基,并且返回
def fp_base(node):

    global dataset
    global minsup

    base_set = {}

    i = 1
    for key in dataset:
        if node in dataset[key]:
            base_set[i] = dataset[key]
            i += 1
    #找出节点存在的所有事务

    for key in base_set:
        base_set[key] = fp_base_pre(base_set[key], node)
    #删除事务中小于node的节点，并且进行排序



    #!需要重新构造一次，问题主要在于base_set中的重复项
    link_set = {}
    temp_set = []
    iter = []
    for key in base_set:#生成组合
        for i in range(1,len(base_set[key]) + 1):
            iter = list(itertools.combinations(base_set[key], i))
            temp_set.append(iter)
        print 'temp_set :'
        print temp_set

        for item_1 in temp_set:
            for item_2 in item_1:
                if item_2 in link_set.keys():
                    item_2 = tuple(item_2)
                    link_set[item_2] += 1
                    #print 'link_set 1'
                    #print link_set
                else:
                    item_2 = tuple(item_2)
                    link_set[item_2] = 1
                    #print 'link_set 2'
                    #print link_set

        temp_key = []
        link_set_keys = []
        for key in link_set:
            link_set_keys.append(key)

        for item in link_set_keys:
            if link_set[item] >= minsup:
                temp_key = list(item)
                temp_key.append(node)
                temp_key = tuple(temp_key)
                link_set[temp_key] = link_set[item]
                del link_set[item]
            else:
                del link_set[item]

    #print 'link_set'
    #print link_set

    return link_set


def fp_growth(tree_form):

    global dataset
    global minsup

    minsup = 5
    fp_set = {}

    for key in tree_form:
        if node != 0:
            fp_set.update(fp_base(key))

    return fp_set


#----------test-------------
global tree, tree_form, sorteditem
global dataset
tree, tree_form, sorteditem = test_fp_tree()

global fp_set, minsup
fp_set = {}
minsup = 5

print tree
print tree_form

path = 'C:\Users\AlanCheg\Desktop\Bank_data_lite.csv'
dataset = csv_to_dataset(path)

sorted_tree_form = tree_form_sorted(tree_form)
print fp_growth(tree_form)
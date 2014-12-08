# -*- coding: UTF8 -*-
from fp_tree import test_fp_tree, node
from csv_to_dataset import csv_to_dataset


#首先，对tree_form 进行排序
def tree_form_sorted(tree_from):

    num_tree_form = {}
    for key in tree_form:
        num_tree_form[key] = tree_form[key][0]
    #将tree_form 的排序元素提取出来

    sorted_tree_form = sorted(num_tree_form.items(), key = lambda asd:asd[1], reverse=False)
    return sorted_tree_form


#删除trans中所有排在node之后的元素，并且将trans递减排序
def fp_base_pre(trans, node):

    global sorteditem
    new_trans = []

    for item in trans:
        if sorteditem.index(item) > sorteditem.index(node):
            new_trans.append(item)
    #找出trans中序号大于node的元素，保存在new_trans中

    len_new_trans = len(new_trans)
    sorted_new_trans = [0] * len_new_trans
    max_node = node

    for i in range(len_new_trans - 1):
        for item in new_trans:
            if sorteditem.index(item) > sorteditem.index(max_node):
                max_node = item
        sorted_new_trans[i] = max_node
        del new_trans[new_trans.index(max_node)]
    #排序

    return sorted_new_trans


#找出节点的条件模式基,并且返回
def fp_base(node):

    global dataset
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


    pass
    #生成tree 和 tree_form


def fp_growth(tree, node):

    global fp_set
    global dataset


def fp_mining(sorted_tree_form):

    global fp_set, minsup

    #for item in sorted_tree_form:
    #    if item[1] >= minsup:
    #        fp_mining_tree(item[0])

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
fp_mining(sorted_tree_form)
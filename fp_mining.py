# -*- coding: UTF8 -*-

from fp_tree import test_fp_tree, node, fp_tree
#from csv_to_dataset import csv_to_data_set
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
    #base_set 是key 从 1 开始的字典

    for key in base_set:
        base_set[key] = fp_base_pre(base_set[key], node)
    #删除事务中排序小于node的节点，并且进行排序
    #因为从树的结构上来看，排序小于node 的节点既是已经遍历过的节点，没有再遍历的意义

    link_set = {}#用于保存每个事务的连接事项，key是项数，value是项数出现的次数
    temp_set = []
    iter_item = []

    for key in base_set:#生成组合
        temp_set = []#初始化防止出现重复项

        for i in range(1,len(base_set[key]) + 1):
            iter_item = list(itertools.combinations(base_set[key], i))
            temp_set.append(iter_item)

        for item_1 in temp_set:#对于每个项数一样的集合
            for item_2 in item_1:#对于集合中的每个元素

                #print item_2
                #print list(item_2)
                temp_item_2 = list(item_2)
                temp_item_2.append(node)
                temp_item_2 = tuple(temp_item_2)

                #temp_item_2 = tuple(list(item_2).append(node))#每个项集都要和node组合

                if temp_item_2 in link_set.keys():
                    link_set[temp_item_2] += 1
                else:
                    link_set[temp_item_2] = 1

        '''
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
        '''

    new_link_set = {}
    for key in link_set:
        if link_set[key] >= minsup:
            new_link_set[key] = link_set[key]
    #删除link_set 中的非fp项集

    return new_link_set


def fp_growth(tree_form):

    global dataset
    global minsup

    minsup = 5
    fp_set = {}

    for key in tree_form:
        if node != 0:
            fp_set.update(fp_base(key))

    return fp_set


def test_fp_mining(out_tree, out_tree_form, out_sorted_item, out_data_set, out_min_sup):

    global tree, tree_form, sorteditem, dataset, fp_set, minsup
    tree = out_tree
    tree_form = out_tree_form
    sorteditem = out_sorted_item
    dataset = out_data_set
    fp_set = {}
    minsup = out_min_sup

    sorted_tree_form = tree_form_sorted(tree_form)
    return fp_growth(tree_form)
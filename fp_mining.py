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


#判断树中是否只有单个路径
def if_single_path(tree):
    pass


def fp_growth(tree, node):

    global fp_set

    if if_single_path(tree):
        pass
    else:
        pass


def fp_mining(sorted_tree_form):

    global fp_set, minsup

    #for item in sorted_tree_form:
    #    if item[1] >= minsup:
    #        fp_mining_tree(item[0])

    return fp_set


#----------test-------------
global tree, tree_form
global dataset
tree, tree_form = test_fp_tree()

global fp_set, minsup
fp_set = {}
minsup = 5

print tree
print tree_form

path = 'C:\Users\AlanCheg\Desktop\Bank_data_lite.csv'
dataset = csv_to_dataset(path)

sorted_tree_form = tree_form_sorted(tree_form)
fp_mining(sorted_tree_form)
# -*- coding: UTF8 -*-

from csv_to_dataset import csv_to_dataset
from fp_pretreatment import fp_pretreatment
from global_var import dataset, tree, tree_from, minsup, now_number, sorteditem #导入全局变量，更加方便

#将trans 按照 sorteditem 的次序生成并且返回 [p|P]
def sort_trans(trans):

    num_dict = {}
    big_num = 0
    for i_1 in range(len(sorteditem) - 1):
        for i in range(len(trans) - 2):
            if sorteditem[i_1][0] == trans[i]:
                num_dict[trans[i]] = sorteditem[i_1][1]

    sorted_num = sorted(num_dict.iteritems(), key = lambda asd:asd[1], reverse = True)
    print sorted_num
    temp = sorted_num[0][0]

    num = 0
    for i in range(len(trans) - 1):
        if temp == trans:
            num = i

    del trans[num]
    return [temp, trans]


#define class node
class node(object):

    def __init__(self):
        self.num = int
        self.level = int
        self.time = int
        self.value = ''
        self.father = int
        self.children = []

    def time_add(self, time):
        self.time += time


def create_fp_tree(father_num, trans, now_level):

    if trans != []:

        now_node_value = sort_trans(trans)[0]
        if_child = 0
        temp_children = tree[father_num].children

        item_number = 0
        for item in temp_children:
            if tree[item].value == now_node_value:
                if_child = 1
                item_number = item
                break

        if if_child == 1:
            tree[item].time += 1
            father_num = item_number
            now_level += 1

            tree_from[tree[item].value][0] += 1

            if trans[1] != []:
                create_fp_tree(father_num, sort_trans(trans)[1], now_level)

        else:
            node_now = node

            node_now.father = father_num
            node_now.num = now_number
            father_num = now_number
            node_now.time += 1
            node_now.value = now_node_value
            node_now.level = now_level
            now_level += 1
            node_now.children = []
            node_now.time += 1

            if node_now.value in tree_from.keys():
                if now_number - 1 in tree_from[node_now.value][1:]:
                    tree_from[node_now.value][0] += 1
                else:
                    tree_from[node_now.value][0] += 1
                    tree_from[node_now.value].append(now_number - 1)
            else:
                tree_from[node_now.value] = [1, now_number - 1]

            if trans[1] != []:
                create_fp_tree(father_num, sort_trans(trans)[1], now_level)


def fp_tree():

    now_number = 0

    tree[now_number] = node
    tree[now_number].num = 0
    tree[now_number].level = 0
    tree[now_number].time = 0
    tree[now_number].value = 'root'
    tree[now_number].father = -1
    tree[now_number].children = []
    #tree 初始化

    tree_from[tree[now_number].value] = [tree[now_number].time]
    for item in tree[now_number].children:
        tree_from[tree[now_number].value].append(item)
    #tree_form 初始化

    now_number += 1

    for i in range(1,len(dataset)):
        create_fp_tree(now_number-1, dataset[i], 1)

    #return tree, tree_from

#------test------------
path = 'C:\Users\AlanCheg\Desktop\Bank_data_lite.csv'
dataset = csv_to_dataset(path)

print "DATASET"
print dataset
print "DATASET END"
#数据预处理，将csv文件的项目按照属性重新生成{ num1 : list1 ; num2 : list2 ; ...}

minsup = 5
#print "SORTED DATASET"

dataset, sorteditem = fp_pretreatment(dataset, minsup)
fp_tree()
print "TREE : "
print tree
print "TREE END"
print "TREE_FORM : "
print tree_from
print "TREE_FORM END"
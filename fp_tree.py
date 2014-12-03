# -*- coding: UTF8 -*-

from csv_to_dataset import csv_to_dataset
from fp_pretreatment import fp_pretreatment
from global_var import dataset, tree, tree_from, minsup, now_number, sorteditem #导入全局变量，更加方便


#将trans 按照 sorteditem 的次序生成并且返回 [p|P]
def sort_trans(trans):

    if len(trans) > 1:
        num_dict = {}

        for i in range(len(sorteditem) - 1):
            for item in trans:
                if sorteditem[i][0] == item:
                    num_dict[item] = sorteditem[i][1]

        sorted_num = sorted(num_dict.iteritems(), key = lambda asd:asd[1], reverse = True)

        node = sorted_num[0][0]
        trans.remove(node)
        return node, trans

    else:

        node = trans[0]
        return node, []


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

        now_node_value, trans = sort_trans(trans)
        #通过函数得到当前事务中排序最高的节点和其他的数据组成的数据集合
        #但是其实每次事务的传递都会导致一次重新排序，因此其实可以优化一下，有空实行

        this_node = node
        this_node.num = now_number
        this_node.father = father_num
        this_node.time = 1
        this_node.value = now_node_value
        this_node.children = []
        this_node.level = now_level
        #初始化当前node

        if_child = 0
        temp_children = tree[father_num].children
        #复制父节点的子节点列表

        item_number = 0
        for item in temp_children:
            if tree[item].value == now_node_value:
                if_child = 1
                item_number = item
                break
        #判断节点node 是否存在于树中的子节点中

        if if_child == 1:#如果它存在于上一个节点的子节点中
            tree[this_node.now_number] = this_node

            tree[item_number].time += 1
            tree[item_number].children.append(now_number)

            now_level += 1

            tree_from[tree[item_number].value][0] += 1
            tree_from[tree[item_number].value].append(now_number)

            father_num = item_number
            create_fp_tree(father_num, trans, now_level)

        else:#如果它不存在于上一个节点的子节点中
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

    for i in range(len(dataset) - 1):
        create_fp_tree(now_number-1, dataset[i + 1], 1)

    #return tree, tree_from

#------test------------
path = 'C:\Users\AlanCheg\Desktop\Bank_data_lite.csv'
dataset = csv_to_dataset(path)
#数据预处理，将csv文件的项目按照属性重新生成{ num1 : list1 ; num2 : list2 ; ...}

minsup = 5
dataset, sorteditem = fp_pretreatment(dataset, minsup)
#对dataset 进行第一次排序，生成属性的排序表 sorteditem
fp_tree()

#对于每一个属性，分派一个序号
print "TREE : "
print tree
print "TREE END"
print "TREE_FORM : "
print tree_from
print "TREE_FORM END"
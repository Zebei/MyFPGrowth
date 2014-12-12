# -*- coding: UTF8 -*-


#sort_trans 直接返回完整的排序序列
def sort_trans(new_trans, trans):

    global sorted_item
    len_sorted_item = len(sorted_item)

    max_num = -1

    if trans != []:
        for item in trans:
            for i in range(len_sorted_item - 1):
                if sorted_item[i][0] == item:
                    if i > max_num:
                        max_num = i

        new_trans.append(sorted_item[max_num][0])
        del trans[trans.index(sorted_item[max_num][0])]

        sort_trans(new_trans, trans)


class MyNode(object):

    def __init__(self):
        self.num = int
        self.level = int
        self.time = int
        self.value = ''
        self.father = int
        self.children = []


def create_fp_tree(father_num, trans, now_level):

    global now_number, tree, tree_form

    if trans != []:

        now_node_value = trans[0]
        del trans[0]
        #通过函数得到当前事务中排序最高的节点和其他的数据组成的数据集合
        #但是其实每次事务的传递都会导致一次重新排序，因此其实可以优化一下，有空实行

        if_child = 0

        temp_children = tree[father_num].children
        #复制父节点的子节点列表

        item_number = 0
        if len(temp_children) != 0:
            for item in temp_children:
                if tree[item].value == now_node_value:
                    if_child = 1
                    item_number = item
            #判断节点node 是否存在于树中的子节点中

        if if_child == 1:#如果它存在于上一个节点的子节点中

            tree[item_number].time += 1
            tree[item_number].children.append(now_number)

            next_now_level =  now_level + 1

            tree_form[tree[item_number].value][0] += 1
            tree_form[tree[item_number].value].append(now_number)

            next_father_num = item_number

            create_fp_tree(next_father_num, trans, next_now_level)

        else:#如果它不存在于上一个节点的子节点中

            this_node = MyNode
            this_node.father = father_num
            this_node.num = now_number
            this_node.value = now_node_value
            this_node.level = now_level
            this_node.children = []
            this_node.time = 1
            #节点初始化

            tree[now_number] = this_node

            next_father_num = now_number
            now_number += 1
            next_now_level = now_level + 1
            #改变层级值和序号值

            if this_node.value in tree_form.keys():
                this_temp = tree_form[this_node.value][1:]
                if next_father_num in this_temp:
                    tree_form[this_node.value][0] += 1
                else:
                    tree_form[this_node.value][0] += 1
                    tree_form[this_node.value].append(next_father_num)
            else:
                tree_form[this_node.value] = [1, next_father_num]
            #将当前节点添加到tree_form

            create_fp_tree(next_father_num, trans, next_now_level)


def fp_tree(data_set, out_sorted_item):

    global now_number, tree, tree_form, sorted_item

    sorted_item = out_sorted_item
    now_number = 0
    tree = {}
    tree_form = {}

    tree[now_number] = MyNode
    tree[now_number].num = 0
    tree[now_number].level = 0
    tree[now_number].time = 0
    tree[now_number].value = 'root'
    tree[now_number].father = -1
    tree[now_number].children = []
    #tree 初始化

    tree_form[tree[now_number].value] = [tree[now_number].time]
    for item in tree[now_number].children:
        tree_form[tree[now_number].value].append(item)
    #tree_form 初始化

    next_father_num = now_number
    now_number += 1

    for key in data_set:
        new_trans = []
        temp = data_set[key]

        sort_trans(new_trans, temp)
        data_set[key] = new_trans

        temp = data_set[key]
        create_fp_tree(0, temp, 1)
    #将数据集合中的所有元素排序
    #trans 是递减的

    return tree, tree_form
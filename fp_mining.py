# -*- coding: UTF8 -*-

from fp_tree import MyNode
import itertools #用于生成排列组合的link

#首先，对tree_form 进行排序
def tree_form_sorted():

    global tree_form

    num_tree_form = {}
    for key in tree_form:
        num_tree_form[key] = tree_form[key][0]
    #将tree_form 的排序元素提取出来

    sorted_tree_form = sorted(num_tree_form.items(), key = lambda asd:asd[1], reverse=False)
    return sorted_tree_form


#找出元素item在sorted_item中的次序
def num_of_sorted_item(item):

    global sorted_item

    for i in range(len(sorted_item) - 1):
        if sorted_item[i][0] == item:
            return i


#删除trans中所有排在node之后的元素，并且将trans递减排序
def fp_base_pre(trans, this_node):

    global sorted_item

    new_trans = []

    for item in trans:
        if num_of_sorted_item(item) > num_of_sorted_item(this_node):
            new_trans.append(item)

    #找出trans中序号大于node的元素，保存在new_trans中

    len_new_trans = len(new_trans)
    sorted_new_trans = [0] * (len_new_trans)
    max_node = this_node

    #注意项集可能为空
    for i in range(len_new_trans):
        max_node = this_node
        for item in new_trans:
            if num_of_sorted_item(item) > num_of_sorted_item(max_node):
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

    global data_set
    global min_sup

    base_set = {}

    i = 1
    for key in data_set:
        if node in data_set[key]:
            base_set[i] = data_set[key]
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

    new_link_set = {}
    for key in link_set:
        if link_set[key] >= min_sup:
            new_link_set[key] = link_set[key]
    #删除link_set 中的非fp项集

    return new_link_set


def fp_growth(sorted_tree_form):

    global data_set
    global min_sup
    global fp_set

    min_sup = 5
    fp_set = {}

    for key in sorted_tree_form:
        this_node = key
        if this_node != 0:
            fp_set.update(fp_base(key))

    return fp_set


def test_fp_mining(out_tree, out_tree_form, out_sorted_item, out_data_set, out_min_sup):

    global tree, tree_form, sorted_item, data_set, fp_set, min_sup

    tree = out_tree
    tree_form = out_tree_form
    sorted_item = out_sorted_item
    data_set = out_data_set
    fp_set = {}
    min_sup = out_min_sup

    sorted_tree_form = tree_form_sorted()
    return fp_growth(sorted_tree_form)
# -*- coding: UTF8 -*-

from fp_tree import MyNode, fp_tree
import itertools  # 用于生成排列组合的link
global tree, tree_form, sorted_item, min_sup


#首先，对tree_form 进行排序 done
#返回的列表序列0是root节点，所以循环建议从1开始
def tree_form_sorted():

    global tree_form

    num_tree_form = {}
    for key in tree_form:
        num_tree_form[key] = tree_form[key][0]
    #将tree_form 的排序元素提取出来

    sorted_tree_form = sorted(num_tree_form.items(), key = lambda asd: asd[1], reverse=False)
    #节点0是root节点，所以循环可以从1开始

    #print 'sorted_tree_form:'
    #print sorted_tree_form
    return sorted_tree_form


#找出元素item在sorted_item中的次序 done
def num_of_sorted_item(this_item):

    global sorted_item
    len_sorted_item = len(sorted_item)

    for i in range(len_sorted_item):
        if sorted_item[i][0] == this_item:
            #print 'i'
            #print i
            return i


#删除trans中所有排在node之后的元素，并且将trans递减排序 done
def fp_base_pre(trans, this_node):

    global sorted_item

    new_trans = []

    for item in trans:
        if num_of_sorted_item(item) > num_of_sorted_item(this_node):
            new_trans.append(item)
        #print 'new_trans:'
        #print new_trans
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
def fp_base(this_node, data_set):

    global min_sup

    #print data_set

    base_set = {}

    i = 1
    for key in data_set:
        if this_node in data_set[key]:
            base_set[i] = data_set[key]
            i += 1
    #找出节点存在的所有事务
    #base_set 是key 从 1 开始的字典

    new_data_set = {} #用于保存项集
    for key in base_set:
        temp_base = base_set[key]
        key_new_data_set = fp_base_pre(temp_base, this_node)
        key_new_data_set = tuple(key_new_data_set)

        if key_new_data_set in new_data_set.keys() and key_new_data_set != ():
            new_data_set[key_new_data_set] += 1
        elif key_new_data_set != ():
            new_data_set[key_new_data_set] = 1
    #删除事务中排序小于node的节点，并且进行排序
    #因为从树的结构上来看，排序小于node 的节点既是已经遍历过的节点，没有再遍历的意义
    #为了简化运算，运用新的字典数据new_data_set ，它的key是项目，value是项目出现的次数

    #print 'new_data_set:'
    #print new_data_set

    link_set = {}#用于保存每个事务的连接事项，key是项数，value是项数出现的次数

    for key in new_data_set:#生成组合

        temp_set = {}#初始化防止出现重复项
        this_key = list(key)

        #for i in range(1,len(base_set[key]) + 1):
        #    it_item = list(itertools.combinations(base_set[key], i))
        #    temp_set.append(it_item)

        for i in range(1,len(this_key) + 1):
            it_item = list(itertools.combinations(this_key, i))
            for item in it_item:
                if tuple(item) in temp_set.keys():
                    temp_set[tuple(item)] += 1
                else:
                    temp_set[tuple(item)] = 1
        #将new_data_set 中的元素随机据结合生成新的字典，key是元素，value是他们出现的次数

        #print 'temp_set'
        #print temp_set

        '''
        for item_1 in temp_set:#对于每个项数一样的集合
            for item_2 in item_1:#对于集合中的每个元素

                #print item_2
                #print list(item_2)
                temp_item_2 = list(item_2)
                temp_item_2.append(this_node)
                temp_item_2 = tuple(temp_item_2)

                if temp_item_2 in link_set.keys():
                    link_set[temp_item_2] += 1
                else:
                    link_set[temp_item_2] = 1
        '''

        for key in temp_set:
            final_temp_key = list(key)
            final_temp_key.append(this_node)
            final_temp_key = tuple(final_temp_key)

            if final_temp_key in link_set.keys():
                link_set[final_temp_key] += temp_set[key]
            else:
                link_set[final_temp_key] = temp_set[key]
#！！！！！！不懂，可能有问题
        #连接所有的元素和node节点

    #print 'link_set'
    #print link_set

    new_link_set = {}
    for key in link_set:
        if link_set[key] >= min_sup:
            new_link_set[key] = link_set[key]
    #删除link_set 中的非fp项集

    #print 'new_link_set:'
    #print new_link_set

    return new_link_set


def fp_growth(out_tree, out_tree_form, out_sorted_item, data_set, out_min_sup):

    global tree, tree_form, sorted_item, min_sup

    tree = out_tree
    tree_form = out_tree_form
    sorted_item = out_sorted_item
    min_sup = out_min_sup

    sorted_tree_form = tree_form_sorted()
    fp_set = {}

    for item in sorted_tree_form:
        this_node = item[0]
        if this_node != 0:
            fp_set.update(fp_base(this_node, data_set))

    return fp_set
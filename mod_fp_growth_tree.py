# -*- coding: UTF8 -*-

#功能：挖掘数据集，生成对应的条件模式树和表格
#输入：dataset（原始数据集），min_sup（最小支持度）
#输出：fp_tree（频繁模式树），fp_tree_form(频繁模式树对应的表格)

#调用：mod_fp_growth_tree(dataset, min_sup)

#test begin -----------------
#from csv_to_dataset import csv_to_dataset
#test end -------------------

#此函数用于生成频繁1项集
def find_frequent_1_itemsets(dataset, min_sup):
#-----
#输入：原始数据集data set和最小支持度min_sup
#输出：频繁1项集
#输入示例：
# {1: [ 'married:NO', 'children:1', 'car:NO', 'save_act:NO', 'current_act:NO', 'mortgage:NO'],
# 2: [ 'married:YES', 'children:3', 'car:YES', 'save_act:NO', 'current_act:YES', 'mortgage:YES']}
#输出示例：
#{('age:66',): 10, ('region:RURAL',): 96}
#good
    ca = {}
    la = {}
    # Ca is the 1 candidate set ,La is the 1 final set

    for key in dataset:
        for item in dataset[key]:
            a = (item,)
            if a in ca.keys():
                ca[a] += 1
            else:
                ca[a] = 1

    for key in ca:
        if ca[key] >= min_sup:
            la[key] = ca[key]
    #print la
    return la


#将经过排序函数生成的元组序列转换成正常的序列
def trans_to_std_set(informal_set):
#输入：排序函数生成的非标准序列
#输出：标准的没有统计次数的序列

    len_informal_set = len(informal_set)
    formal_set = [0]*len_informal_set

    for i in range(len_informal_set):
        temp = informal_set[i][0][0]
        formal_set[i] = temp

    return formal_set


#此函数主要用于返回元素a在序列set中的序号
def num_in_order(a, order_set):

    set_len = len(order_set)
    for i in range(set_len):
        if order_set[i] == a:
            return i
        else:
            pass


#此函数的主要功能是将input_set中的元素按照order_set中的
#顺序排列并且生成新的序列new_order_set 并且输出
def new_order_set(order_set, input_set):
#——————
#其中，order_set 是由排序函数生成的序列，input_set是数据集中的一列数据
#new_order_set是新生成的格式与input_set一样的
#——————
#实现方法是先生成一个input_set的序列字典new_dic
#再通过冒泡排序生成新的序列

    new_dic = {}
    num = 0
    temp = ''
    #order_set = trans_to_std_set(order_set)
    #new_dic是用于存储input_set在order_set中序号值的字典

    for item in input_set:
        num = num_in_order(item ,order_set)
        new_dic[item] = num

    input_set_len = len(input_set)
    for i in range(input_set_len):
        for j in range((input_set_len - i) -1):
            if new_dic[input_set[j]] <= new_dic[input_set[j + 1]]:
                pass
            else:
                temp = input_set[j]
                input_set[j] = input_set[j + 1]
                input_set[j + 1] = temp
                temp = ''

    return input_set


#此函数主要用于将树的statistics_form按照出现计数递减排序
def statistics_form_sort(statistics_form):

    i = 0
    sorted_statistics_form = []
    key_in_statistics_form = []

    #生成key的序列，便于之后的遍历
    for key in statistics_form:
        key_in_statistics_form.append(key)

    len_form = len(key_in_statistics_form) - 1
    sorted_statistics_form = [0]*len_form
    for i in range(len_form):
        big_key = 0
        node = []
        for j in range((len(key_in_statistics_form) - 1)):
            if statistics_form[key_in_statistics_form[j]][0] > statistics_form[key_in_statistics_form[big_key]][0]:
                big_key = j
        node = [key_in_statistics_form[big_key],statistics_form[key_in_statistics_form[big_key]]]
        sorted_statistics_form[i] = node
        del statistics_form[key_in_statistics_form[big_key]]
        del key_in_statistics_form[big_key]

    #print 'sorted_statistics_form begin'
    #print sorted_statistics_form
    #print 'sorted_statistics_form end'
    return sorted_statistics_form


#经过第一次遍历，生成一棵fp_growth_1st_tree
#并且返回数的结构以及排序之后的节点
def fp_growth_1st_tree(dataset, min_sup):

    fp_tree = {}
    root = ('null', 'root')
    fp_tree[root] = {}
    fp_tree[root]['root'] = True
    fp_tree[root]['key'] = 1
    fp_tree[root]['father'] = ''
    fp_tree[root]['children'] = []
    #初始化根节点
    #fp_tree 是第一次遍历生成的树

    c_1 = find_frequent_1_itemsets(dataset, min_sup)
    sorted_c_1 = sorted(c_1.items(), key=lambda asd: asd[1], reverse=True)
    #asd[0] 为键，asd[1] 为键值
    formal_sorted_set = trans_to_std_set(sorted_c_1)
    #min_sup是最小支持度
    #c_1是对起始数据集第一次扫描所生成的待选数据集合
    #sorted_c_1是将c_1中的属性按键值递减排序生成的元组列表
    #formal_sorted_set是将sorted_c_1只有属性的递减列表
    #print formal_sorted_set

    statistics_form = {}
    #statistics_form是用于检索树结构的项头表

    #用于生成树，树由字典组成，关键字是一个包含层数和属性名的元组。
    #值是一个由四个关键字key,root,father,children组成的字典
    #key = int, root = bool, father = '', children = []
    for key in dataset:
        sorted_list = new_order_set(formal_sorted_set, dataset[key])
        #返回的序列第一项都是id，正好可以去除掉。

        j = 1
        for i in range(1, len(sorted_list)):
            item = sorted_list[i]
            node = (j, item)
            if item not in statistics_form:
                statistics_form[item] = [0, []]

            if i == 1:
                if node in fp_tree[root]['children']:
                    fp_tree[node]['key'] += 1
                    pre_node = node
                    statistics_form[item][0] += 1
                    if node in statistics_form[item][1]:
                        pass
                    else:
                        statistics_form[item][1].append(node)
                else:
                    fp_tree[root]['children'].append(node)
                    fp_tree[node] = {}
                    fp_tree[node]['root'] = False
                    fp_tree[node]['key'] = 1
                    fp_tree[node]['father'] = 'root'
                    fp_tree[node]['children'] = []
                    pre_node = node
                    statistics_form[item][0] += 1
                    if node in statistics_form[item][1]:
                        pass
                    else:
                        statistics_form[item][1].append(node)
            else:
                if node in fp_tree[pre_node]['children']:
                    fp_tree[node]['key'] += 1
                    pre_node = node
                    statistics_form[item][0] += 1
                    if node in statistics_form[item][1]:
                        pass
                    else:
                        statistics_form[item][1].append(node)
                else:
                    fp_tree[node] = {}
                    fp_tree[pre_node]['children'].append(node)
                    fp_tree[node]['root'] = False
                    fp_tree[node]['key'] = 1
                    fp_tree[node]['father'] = pre_node
                    fp_tree[node]['children'] = []
                    pre_node = node
                    statistics_form[item][0] += 1
                    if node in statistics_form[item][1]:
                        pass
                    else:
                        statistics_form[item][1].append(node)

            j += 1
    sorted_statistics_form = statistics_form_sort(statistics_form)
    #print 'fp_tree, sorted_statistics_form begin'
    #print fp_tree, sorted_statistics_form
    #print 'fp_tree, sorted_statistics_form end'
    return fp_tree, sorted_statistics_form


#此函数的功能是统一使用前面的函数，并且返回频繁模式树 和 对应的表列
def mod_fp_growth_tree(dataset, min_sup):

    fp_1st_tree, statistics_form = fp_growth_1st_tree(dataset, min_sup)

    #print fp_1st_tree
    #print statistics_form
    return fp_1st_tree,statistics_form

'''
#test begin ------------------
path = 'C:\Users\AlanCheg\Desktop\DataMining\Bank-data.csv'
dataset = csv_to_dataset(path)
mod_fp_growth_tree(dataset, 20)
#test end --------------------
'''
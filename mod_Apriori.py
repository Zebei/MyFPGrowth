# -*- coding: UTF8 -*-

"""
——————
mod_Apriori
——————
Apriori算法模块
——————
输入：由csv_to_dataset模块产生的字典嵌套集合
输出：k项集（k = 1，2，。。）的字典集合
——————
经过实际使用，发现算法效率非常低
后面需要研究如何提升算法效率
——————
"""


def find_frequent_1_itemsets(dataset, min_sup):
#此函数用于生成1项集
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

    return la


def apriori_gen(l):
#此函数使用了先验性质，通过已有集合l(k - 1)生成新的候选集合c(k)
#c_all 用于保存所有的数据集；字典类型
#ca用于保存关键字candi及其数字；字典类型
#candi用于保存关键字；元组类型

    c_all = {}

    #print l
    #print 'test'

    for key_1 in l:
        for key_2 in l:
            linkable = 1
            ca = {}
            candi = ()

            if len(key_1) >= 2:

                #print 'good'

                key_len = len(key_1)

                for i in range(key_len - 2):
                    if key_1[i] != key_2[i]:
                        linkable = 0

                #print 'good'
                #print linkable

                if key_1[len(key_1)-1] >= key_2[len(key_2)-1]:
                    linkable = 0

                #print 'good'
                #print linkable

                if linkable == 1:
                    candi = apriori_link(key_1, key_2)
                    ca[candi] = 0

                #print candi
                #print 'good'

                if has_infrequent_subset(candi, l):
                    pass
                else:
                    c_all = dict(c_all, **ca)

            else:
            #good
                if key_1 < key_2:
                    new_set = apriori_link(key_1, key_2)

                    candi = new_set
                    c_all[candi] = 0

                else:
                    pass

    return c_all


def scan_to_l(candidate, dataset, support):
#扫描候选集合中集合在数据集D中的支持度，返回最终集合
#输入的是待选集c(k) k > 1，产生的是确定集合l(k)
#good

    l = {}

    for key_1 in candidate:
        for key_2 in dataset:
            if item_in_dataset(key_1, dataset[key_2]):
                candidate[key_1] += 1

    for key_1 in candidate:
        if candidate[key_1] >= support:
            l[key_1] = candidate[key_1]

    return l


def item_in_dataset(item_candidate, item_dataset):
# 检查给定的待选数据是否在给定的完整数据集项目中，若是返回True，否则为False

    if_in_item = 0

    for item_1 in item_candidate:
        for item_2 in item_dataset:
            if item_1 == item_2:
                if_in_item += 1
            else:
                pass

    if if_in_item == len(item_candidate):
        return True
    else:
        return False


def apriori_link(set_1, set_2):
#链接给定的两个数据集
#good

    set_1 = list(set_1)
    set_2 = list(set_2)

    set_1.append(set_2[len(set_2) - 1])
    set_1 = tuple(set_1)

    return set_1


def has_infrequent_subset(candidate, l):
#candidate is (k) set ,l is (k -1) set
#查看给定的待选集中是否含有 k - 1 项集中没有的集合
#实现方法为先将candidate转化为n个(k-1)项集，若他们都在l中，则返回True
#否则返回False

    new_candidate = {}
    candi_len = len(candidate)

    for i in range(candi_len):
        candidate_copy = list(candidate)
        del candidate_copy[i]
        new_candidate[tuple(candidate_copy)] = 0

    new_candi_len = len(new_candidate)
    num_frequent = 0

    for key in new_candidate:
        if key in l:
            num_frequent += 1

    if num_frequent == new_candi_len:
        return False
    else:
        return True


def mod_apriori(dataset, min_sup):
    l_set = find_frequent_1_itemsets(dataset, min_sup)
    #print l_set

    c_set = l_set
    while c_set != {}:
        c_set = l_set
        print c_set
        c_set = apriori_gen(l_set)
        l_set = scan_to_l(c_set, dataset, min_sup)
        print l_set
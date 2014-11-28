# -*- coding: UTF8 -*-

#功能：对数据集合进行fp_growth挖掘，并且返回频繁项集
#输入：dataset（原始数据集），min_sup（最小支持度）
#输出:fp_set (频繁项集)

#调用：mod_fp_growth(dataset, min_sup)

from mod_fp_growth_tree import mod_fp_growth_tree
from mod_fp_growth_mining import mod_fp_growth_mining


#执行FP_Growth算法的一系列操作，便于函数调用
def mod_fp_growth(data, min_sup):

    fp_tree, fp_tree_form = mod_fp_growth_tree(data, min_sup)
    print 'FP_TREE : '
    print fp_tree
    print 'FP_TREE_FORM : '
    print fp_tree_form #显示生成的数据格式，便于后期调试

    fp_set = mod_fp_growth_mining(fp_tree, fp_tree_form, min_sup)
    return fp_set

'''
    global frequent_pattern
    frequent_pattern = []
    #fp_1st_tree是树结构，statistics_form是存每个结构的指向表格
    #接下来对statistics_form 做一次排序，生成sorted_statistics_form
    #在此函数内部做了改变，返回的statistics_form是已经排序过的序列
    fp_1st_tree, statistics_form = fp_growth_1st_tree(dataset, min_sup)
    print fp_1st_tree
    print statistics_form
    fp_iter(fp_1st_tree, statistics_form, min_sup)
    print frequent_pattern
'''
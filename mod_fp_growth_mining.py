# -*- coding: UTF8 -*-

#功能：挖掘频繁模式树
#输入：fp_tree （频繁模式树）, fp_tree_form(频繁模式树对应的表列)，min_sup(最小支持度)
#输出:fp_set (频繁项集)

#调用：mod_fp_growth_mining(fp_tree, fp_tree_form, min_sup)

from mod_fp_growth_mining_node import mod_fp_growth_mining_node
from mod_fp_growth_mining_forest import mod_fp_growth_mining_forest
from mod_fp_growth_mining_miner import mod_fp_growth_mining_miner


'''
#对于输入的tree_line,生成关于它的频繁项集，并且增加到frequent_pattern中
#——————————
#输入：fp_tree以及一条树中的枝
def tree_line_link(fp_tree, tree_line, min_sup):

    count_j = 0
    #print tree_line
    #print tree_line
    for i in range(len(tree_line) - 1):
        if fp_tree[tree_line[count_j]]['key'] < min_sup:
            #print fp_tree[tree_line[count_j]]['key']
            del tree_line[count_j]
        else:
            count_j += 1


#————————*
def fp_base_forest_link(node, forest, forest_form, min_sup):
#主要的作用是将导入的节点node 和它的条件模式森林，森林表列链接，并且返回频繁项集
#返回的是有此节点的频繁项集

    fp_set = {}
    node_temp = []

    #第一步，与每个单节点连接
    for key in forest_form:
        if key != node:
            node_temp = [key, node]
            fp_set[tuple(node_temp)] = forest_form[key][0]

    #调用函数进行连接操作，并且返回对对应的数据项集
    fp_set = link_all(forest, forest_form, node, min_sup)
    return fp_set


#待改正
def fp_mining(line, node, min_sup):
#————————
#此函数将被递归调用，所以每次只用考虑输入为
#line 是节点node 在树中的所有枝，node 是待挖掘节点，min_sup 是最小支持度计数
#————————
#此函数的主要功能是首先生成节点node 的条件模式树，并且生成它的指向表格
#然后找出树中大于（有的节点在一棵树中的出现次数小于最小支持度，但是在整个森林中
#出现的次数是大于min_sup 的，这些不要误剪枝，所以先生成森林，再进行剪枝操作）
#最小支持度的所有节点，与node 连接，生成频繁模式
#连接时注意，出现频度为所有节点中出现次数最小的那个，同时，需要注意的是，一组
#频繁模式当中，出现频度只能计算当它们在同一棵树中的情况，而不是计算整个森林中各个节点的
#出现情况
#————————

    base_foreast= []
    base_tree = {}



    print node
    print line
'''


#用于调用函数，并且返回值
def mod_fp_growth_mining(fp_tree, fp_tree_form, min_sup):
    #fp_set = {}
    normal_node = ''
    line = {}

    for i in range(len(fp_tree_form) - 1):

        normal_node = fp_tree_form[len(fp_tree_form) - 1 - i]
        line = (fp_tree, fp_tree_form, normal_node, min_sup)

        print "NODE + LINE : "
        print normal_node, line
        print "NODE + LINE END"#便于分析

        forest, forest_form = mod_fp_growth_mining_forest(line, min_sup)
        print 'number:' + i
        print forest, forest_form
        print 'end'
        #fp_set = mod_fp_growth_mining_miner(normal_node, forest, forest_form, fp_set)

    #return fp_set
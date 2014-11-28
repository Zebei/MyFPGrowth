# -*- coding: UTF8 -*-

#功能：对于给定的fp_tree（条件模式树），通过fp_tree_form检索并且返回节点以及它对应的所有的枝
#输入：fp_tree, fp_tree_form, min_sup
#输出：node, line

#调用：mod_fp_growth_mining_node(fp_tree, fp_tree_form, node, min_sup)
#返回值：node 对应的所有枝的集合 line


#对于输入的子节点node，找出它在fp_tree中所在的链,并且调用函数来寻找其中存在的频繁项集
def fp_growth(fp_tree, fp_tree_form, node, min_sup):
#输入：fp_tree以及节点node
#此函数的输出将作为节点node的条件模式基，用于生成node的树

    line = {}
    node_child = len(node[1][1])
    for i in range(node_child):
        node_now = node[1][1][i]
        node_prev = node_now
        line_now = []
        while fp_tree[node_now]['father'] != 'root':
            #print node_now
            line_now.append(node_now)
            node_prev = node_now
            node_now = fp_tree[node_now]['father']
        line_now.append(node_now)
        line[tuple(line_now)] = fp_tree[node_prev]['key']
        #生成了node节点的枝的列表line,作为条件模式基

    return line


def mod_fp_growth_mining_node(fp_tree, fp_tree_form, node, min_sup):

    line = fp_growth(fp_tree, fp_tree_form, node, min_sup)
    return line
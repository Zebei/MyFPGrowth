# -*- coding: UTF8 -*-

#功能：对于给定的node 和 它的所有枝的集合 line，生成它的条件模式森林和对应的表格
#输入：line（节点node 所有的枝的集合），min_sup（最小支持度）
#输出：forest（node 的条件模式森林），forest_form（forest 的对应地址表）

#调用：mod_fp_growth_mining_forest(line, min_sup)


'''
#此函数的主要功能是将line 反转并且返回,因为标准输出的line是倒叙排列的
def branch_reverse(line):

    line_reverse = []
    line_len = len(line)
    line_reverse = [0] * line_len
    a = 0
    for i in range(line_len - 1):
        a = line_len - i - 1
        line_reverse[a] = line[i]

    return line_reverse
'''


#对应给定的树和节点，返回它在这棵树中的子节点
def find_children_node(tree, father_node):

    for key in tree:
        if father_node[1] == key[0]:
            return key


#找出tree 中层数为j的节点并且返回，root 层作为第0 层
def find_j_node(tree, j):

    j_node = []
    for key in tree:
        if key[0] == 'root':
            j_node = list(key)

    j_node = tuple(j_node)

    if j == 0:
        return j_node
    else:
        for i in range(j - 1):
            j_node = find_children_node(tree, j_node)

        return j_node


#当枝无法合并到已有的枝时，将一个枝转换成一棵树
def branch_2_new_tree(branch, branch_num, forest, forest_form):

    tree = {}
    #root = []
    all_form_keys = []

    for key in forest_form:
        all_form_keys.append(key)

    father_node = 'root'
    for item in branch:
        node = [father_node, item[1], branch_num]

        if item[1] in all_form_keys:

            forest_form[item[1]][0] += branch_num

            all_node_keys = []
            for key in forest_form[item[1]][1]:
                all_node_keys.append(key)

            node_temp_1 = (branch[0], node[0], node[1])
            if node_temp_1 not in all_node_keys:
                forest_form[item[1]][1][node_temp_1] = branch_num

            forest_form[item[1]][1][branch[0]] = item

        else:

            node_temp_1 = (branch[0], node[0], node[1])
            forest_form[item[1]] = [] * 2
            forest_form[item[1]][0] = branch_num
            forest_form[item[1]][1] = {}
            forest_form[item[1]][1][node_temp_1] = branch_num

        tree[(node[0], node[1])] = node[2]
        father_node = item[1]

    forest[branch[0]] = tree
    return forest, forest_form


#当枝节点能合并到森林中的某一个节点时，将它并到已有的树中
def branch_2_old_tree(branch, branch_num, forest, forest_form):

#数据格式：
#branch = (node1, node2, node3, ...)  branch_num = int
#node = (num, value)

    tree = forest[branch[0]]

    all_tree_keys = []
    all_form_keys = []
    for key in tree:
        all_tree_keys.append(key)
    for key in forest_form:
        all_form_keys.append(key)

    prev_item = ['root','root']

#将branch 填充到已有的树中，或者生成一棵新树
    branch_len = len(branch)
    j = 0
    j_node = []

    for i in range(branch_len - 1):
        j = i
        j_node = find_children_node(tree, j)
        now_node = (prev_item[0], branch[i][1])

        if j_node == now_node:

            tree[j_node] += branch_num
            forest_form[branch[i][1]][1] += branch_num
            temp_node_1 = (branch[0][1], prev_item[1], branch[i][1])
            forest_form[branch[i][1]][temp_node_1] += branch_num

        else:

            new_tree_node = (branch[0][1], branch[i][1])
            tree[new_tree_node] = branch_num
            forest_form[branch[i][1]][0] += branch_num

            new_form_node = (branch[0][1], prev_item[1], branch[i][1])
            forest_form[branch[i][1]][1][new_form_node] = branch_num

        prev_item = branch[i]

    forest[branch[0]] = tree
    return forest, forest_form


#用给出的节点所在的枝，生成相对应的森林，并且为了方便森林的读取，会同时生成一个地址表
def fp_base_forest(line, min_sup):
#————————
#输入：line 节点的枝的集合，min_sup
#输出：node 的条件模式基生成的森林
#line 的格式为 line = {(node1,node2,...):num; (...)...}
#min_sup 是一个int 型的整数
#————————
#数据说明：
#forest_form 的数据格式为 {node1: [node_num,[(tree1, father_node1, now_node1, node_num),(...)] ; ...}
#forest 的数据格式为 Forest =｛root1：tree1； root2， tree2； ...｝
#tree 的数据格式为 Tree = {(father_node1, now_node1)：node_num; (father_node2, now_node2): node_num ; ... }
#————————

    forest_form = {}
    forest = {}
    all_root = []

    for key in line:

        single_line = key
        branch = []
        for key_1 in single_line:
            branch.append(key_1)
        print 'BRANCH : '
        print branch
        print 'BRANCH END'

        branch_num = line[key]
        #len_branch = len(branch)
        #经过反转除理的枝，和它的频度，长度属性

        for key in forest:
            all_root.append(key)

        if branch[0] in all_root:
            forest, forest_form = branch_2_old_tree(branch, branch_num, forest. forest_form)
        else:
            forest, forest_form = branch_2_new_tree(branch, branch_num, forest, forest_form)

    for key in forest_form:
        if forest_form[key] < min_sup:
            del forest_form[key]
    #对forest_form 进行剪枝

    return forest, forest_form


#主要的作用是作为标准接口，防止文件更改导致程序出错
def mod_fp_growth_mining_forest(line, min_sup):

    forest, forest_form = fp_base_forest(line, min_sup)
    return forest, forest_form
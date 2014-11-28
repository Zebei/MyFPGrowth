# -*- coding: UTF8 -*-

#功能：挖掘频繁模式树
#输入：node（指定节点）, forest（node 的条件模式森林），forest_form（forest 的对应地址表）,fp_set（频繁项集）（在已有的频繁项集上添加）
#输出:fp_set (频繁项集)

#调用：mod_fp_growth_mining_miner(node, forest, forest_form)


#————————fp_base_forest_link
#对一个节点的条件模式基 生成并且返回频繁模式
def link_all(forest, forest_form, node, min_sup):
#此函数用于将数据集和node 连接并且返回频繁项集
    fp_set = {}
    fp_set_return = {}

    #将树中的所有节点检索出来，便于后续的查找与定位
    all_set_keys = {}
    for key_forest in forest:#每棵树
        all_set_keys[key_forest] = []
        for key_tree in forest[key_forest]:#树中的每个节点
            all_set_keys[key_forest].append(key_tree)

    #计算树的长度，用于确定递归次数
    temp_key_1 = []
    for key in forest_form:
        temp_key_1.append(key)

    #linkable_node_num = 0
    linkable_node_num = len(temp_key_1) - 1#- 1是因为原节点也会存在于forest_form中

    #fp_tree 的连接
    fp_set[1] = {}
    temp_fp_node = []

    max_time = 0
    #找出最大的节点次数
    for key in forest:
        if len_of_keys(forest[key]) >= max_time:
            max_time = len_of_keys(forest[key])

    #生成第一层的节点，便于之后调用递归程序
    for key_fo in forest:
        for key_tr in forest[key]:
            fp_set[1][key_fo][key_tr[1]] = forest[key_fo][key_tr]

    #递归得到所有的节点
    fp_set = link_node(fp_set, 2, max_time)

    #连接fp_set 与 node,并且生成频繁模式
    for key_fp in fp_set:#每一层
        for key_fp_tr in fp_set[key_fp]:#每层中的每棵树
            for key_node in fp_set[key_fp][key_fp_tr]:

                if key_fp == 1:#如果是第一层的节点，那么值在forest_form中找
                    fp_set_return[(key_node, node[0][1])] = forest_form[key_fp_tr][0]
                else:
                    fp_set_return[tuple(list(key_node).append(node[0][1]))] = fp_set[key_fp][key_fp_tr][key_node]

    return fp_set_return

'''
        if key != node[0][1]:
            temp_fp_node = [key, node[0][1]]
            fp[1][tuple(temp_fp_node)] = forest_form[key][0]


    #生成频繁二项集，之后的k项集距可以由k - 1（k > 2） 项集聚合而成
    #但是，需要注意的是，能组成k项集的所有k - 1 项集必须属于同一棵树


    #now code begin
    #此段代码的主要功能是用循环生成连接节点

    #遍历所有的节点，并且生成可以和node 连接的条件模式基
    #对于n节点，生成方法是采用n - 1 次节点连接而成
    #但是为了保证算法的简易性，1 次节点也得使用此方法，但是在进行链接的时候，应当注意，1次
    #节点对应的值不能需要使用forest_form当中的值才行
    keys_in_forest = []
    for key in forest_form:

        for key_2 in forest:
            keys_in_forest.append(key_2)

        tree_num = len(keys_in_forest)#统计树的个数，同时便于树的定位

        for i in range(len(key) - 1)：
            for key_1 in
                if key != node[0][1]:
                    temp_fp_node = [key, node[0][1]]
                    fp[1][][i][tuple(temp_fp_node)] = forest_form[key][0]


    #new code end


    for i in range(1, linkable_node_num - 1):

        fp_set[i + 1] = {}

        pass
'''


#用于生成连接点的函数，单独列出，方便递归
#n > 1
def link_node(fp_set, n, max_time):
#接受的值是fp_set 数据集，以及n = 已经待递归的次数,max是指能够生成的最大项集的数目
#当待递归次数等于0 时，返回fp_set ，否则递归调用自身

    new_node = []
    if n == max_time:
        return fp_set
    else:
        for key in fp_set[n]:

            for key_1 in fp_set[n][key]:
                for key_2 in fp_set[n][key]:

                    if if_linkable(key_1,key_2):
                        new_node = linkable_node_link(key_1, key_2)

                        keys_in_set_temp = []
                        for key_3 in fp_set[n + 1]:
                            keys_in_set_temp.append(key_3)

                        if new_node not in keys_in_set_temp:

                            if fp_set[n][key][key_1] < fp_set[n][key][key_2]:
                                fp_set[n + 1][key][key_3] = fp_set[n][key][key_1]
                            else:
                                fp_set[n + 1][key][key_3] = fp_set[n][key][key_2]

        link_node(fp_set, n - 1, max_time)
###################################


#判断两个节点是否可以连接
#node1 和 node2 是 fp_node 型数据
def if_linkable(node1, node2):

    count = 0

    for item in node1:
        if item in node2:
            count += 1

    if count == (len(node1) - 1):
        return True
    else:
        return False
#############################


#link 两个可以连接的节点,并且返回新的节点
def linkable_node_link(node1, node2):

    new_node = node1[0]

    for item in node1:
        if item not in node2:
            new_node = item

    node2.append(new_node)
    return node2


#用于计算列表中的元素数目并且返回
def len_of_keys(dic_1):

    a = []

    for key in dic_1:
        a.append(key)

    return len(a)
####################################


def mod_fp_growth_mining_miner(node, forest, forest_form, fp_set):
    pass
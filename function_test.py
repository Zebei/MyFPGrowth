# -*- coding: UTF8 -*-


def num_in_order(a, set):
#此函数主要用于返回元素a在序列set中的序号
    set_len = len(set)
    for i in range(set_len):
        if set[i] == a:
            return i

def new_order_set(order_set ,input_set):
#——————
#此函数的主要功能是将input_set中的元素按照order_set中的
#顺序排列并且生成新的序列new_order_set 并且输出
#——————
#其中，order_set 是由排序函数生成的序列，input_set是数据集中的一列数据
#new_order_set是新生成的格式与input_set一样的
#——————
#实现方法是先生成一个input_set的序列字典new_dic
#再通过冒泡排序生成新的序列
#——————

    new_dic = {}
    num = 0
    temp = ''

    for item in input_set:
        num = num_in_order(item ,order_set)
        new_dic[item] = num

    input_set_len = len(input_set)
    for i in range(input_set_len):
        for j in range((input_set_len - i - 1)):
            if new_dic[input_set[j]] <= new_dic[input_set[j + 1]]:
                pass
            else:
                temp = input_set[j]
                input_set[j] = input_set[j + 1]
                input_set[j + 1] = temp
                temp = ''

    return input_set


input_set = [1,2,3,4,5,6,7]
order_set = [7,5,6,4,3,2,1,0]

print new_order_set(order_set, input_set)
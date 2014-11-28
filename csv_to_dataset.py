# -*- coding: UTF8 -*-

'''
——————
这个程序主要是将.csv 文件转换成其他算法可用的数据集合dataset
例如用于Apriori以及FP-growth算法中。
——————
输入：.csv文件
输出：按每行区分的字典数据集合
输出数据示例：
{1: ['id:ID12101', 'age:48', 'sex:FEMALE', 'region:INNER_CITY', 'income:17546.0', 'married:NO', 'children:1', 'car:NO', 'save_act:NO', 'current_act:NO', 'mortgage:NO'],
2: ['id:ID12102', 'age:40', 'sex:MALE', 'region:TOWN', 'income:30085.1', 'married:YES', 'children:3', 'car:YES', 'save_act:NO', 'current_act:YES', 'mortgage:YES']}
——————
'''


def csv_to_dataset(path):
    d_all ={}
    d_item = []
    str_value = ''
    str = ''
    i_item = 0

    with open(path, 'r') as f:
        for line in f.readlines():
            str = ''
            i_no = 0
            if i_item == 0:
                for word in line:
                    if word == ',':
                        d_item.append(str)
                        str = ''
                    else:
                        str += word
            else:
                d_all[i_item] = []
                for word in line:
                    if word == ',':
                        key_word = d_item[i_no]
                        str_value = key_word
                        str_value += ':'
                        str = str_value + str
                        d_all[i_item].append(str)
                        i_no += 1
                        str = ''
                    elif word == '\\' or word == 'n':
                        pass
                    else:
                        str += word
            i_item += 1
    #print d_all
    return d_all

'''
----
test code
----

#path = raw_input('print path: ')
path = 'C:\Users\AlanCheg\Desktop\DataMining\Bank-data.csv'
d_all = csv_to_dataset(path)
for key in d_all:
    print key
    print d_all[key]
'''
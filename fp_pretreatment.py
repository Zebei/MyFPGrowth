# -*- coding: UTF8 -*-

#将数据集传过来的数据进行预处理，即对数据进行第一次排序，并且删除小于最小支持度的节点

from csv_to_dataset import csv_to_dataset
from collections import defaultdict

#------test------------
path = 'C:\Users\AlanCheg\Desktop\Bank_data_lite.csv'
dataset = csv_to_dataset(path)
print dataset
#数据预处理，将csv文件的项目按照属性重新生成{ num1 : list1 ; num2 : list2 ; ...}


minsup = 5
dict_1 = {}
all_keys = []
for i in dataset:

    all_keys = []
    for key in dict_1:
        all_keys.append(key)

    for item in dataset[i]:
        if item in all_keys:
            dict_1[item] += 1
        else:
            dict_1[item] = 1

'''
real_dict = {}
for key in dict_1:
    if dict_1[key] >= minsup:
        real_dict[key]  = dict_1[key]
'''

print "1_DICT : "
print dict_1


i = 0
sorteditem = [0] * [i + 1 for key in dict_1]
#初始化一个和dict 的 key 数目一样的 list















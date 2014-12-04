# -*- coding: UTF8 -*-
#将数据集传过来的数据进行预处理，即对数据进行第一次排序，并且删除小于最小支持度的节点
from csv_to_dataset import csv_to_dataset
from collections import defaultdict

# 返回 dataset, sorteditem

def fp_pretreatment(dataset, minsup):

    dict_1 = {} #第一次挖掘生成的频繁项集
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

    #print "DICT_1 : "
    #print dict_1
    #print "DICT_1 END"

    #对dict_1 进行排序，并且生成有序节点
    i = 0
    sorteditem = sorted(dict_1.iteritems(), key = lambda asd:asd[1], reverse = True)

    #print "SORTED DATASET"
    #print sorteditem
    #print "SORTED DATASET END"

    return dataset, sorteditem


#------test------------
path = 'C:\Users\AlanCheg\Desktop\Bank_data_lite.csv'
dataset = csv_to_dataset(path)

print "DATASET"
print dataset
print "DATASET END"
#数据预处理，将csv文件的项目按照属性重新生成{ num1 : list1 ; num2 : list2 ; ...}
minsup = 5
#print "SORTED DATASET"
fp_pretreatment(dataset, minsup)
# -*- coding: UTF8 -*-

from csv_to_dataset import csv_to_data_set  # import
from fp_pretreatment import fp_pretreatment
from fp_tree import fp_tree
from fp_mining import fp_growth

print 'This is a python program to achieve fp_growth!'
file_path = raw_input('Please input the path of your file(now only support .csv file) : ')
min_sup = raw_input('Please input the min_sup : ')

if file_path == '':
    file_path = 'C:\Users\AlanCheg\Desktop\Bank_data_lite.csv'  # default
if min_sup == '':
    min_sup = 3   # default

data_set = csv_to_data_set(file_path)
other_data_set = data_set
sorted_item = fp_pretreatment(data_set)
tree, tree_form = fp_tree(data_set, sorted_item)  # 改变了data_set 的值

data_set = csv_to_data_set(file_path)
fp_set = fp_growth(tree, tree_form, sorted_item, data_set, min_sup)
print fp_set
# -*- coding: UTF8 -*-

from csv_to_dataset import csv_to_data_set  # import
from fp_pretreatment import fp_pretreatment
from fp_tree import fp_tree
from fp_mining import test_fp_mining

print 'This is a python program to achieve fp_growth!'
file_path = raw_input('Please input the path of your file(now only support .csv file) : ')
min_sup = raw_input('Please input the min_sup : ')

if file_path == '':
    file_path = 'C:\Users\AlanCheg\Desktop\DataMining\Bank-data.csv'  # default
if min_sup == '':
    min_sup = 20   # default

data_set = csv_to_data_set(file_path)
sorted_item = fp_pretreatment(data_set)
tree, tree_form = fp_tree(data_set, sorted_item)
fp_set = test_fp_mining(tree, tree_form, sorted_item, data_set, min_sup)
print fp_set

'''
end = '0'
while end == '0':
    i = raw_input('1. Aprori ; 2. FP-Growth ; 3.Exit:')
    if i == '1':
        mod_apriori(data, min_sup)
    elif i == '2':
        mod_fp_growth(data, min_sup)
    elif i == '3':
        end = 1
    else:
        print 'Input wrong!'
'''
# -*- coding: UTF8 -*-

from mod_Apriori import mod_apriori
from csv_to_dataset import csv_to_dataset
from mod_fp_growth import mod_fp_growth
#from matplotlib_test import *

path = 'C:\Users\AlanCheg\Desktop\DataMining\Bank-data.csv'
data = csv_to_dataset(path)
min_sup = 20

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
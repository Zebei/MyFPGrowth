# -*- coding: UTF8 -*-

#这个程序主要是将.csv 文件转换成其他算法可用的数据集合data_set
#例如用于 apriori 以及FP-growth算法中。
#输入：.csv文件
#输出：按每行区分的字典数据集合


def csv_to_data_set(path):
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

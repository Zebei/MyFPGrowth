# -*- coding: UTF8 -*-

#将数据集传过来的数据进行预处理，即对数据进行第一次排序
#返回 排序元素集合 sorted_item


def fp_pretreatment(data_set):

    dict_1 = {}  # 第一次挖掘生成的频繁项集

    for i in data_set:
        all_keys = []
        for key in dict_1:
            all_keys.append(key)

        for item in data_set[i]:
            if item in all_keys:
                dict_1[item] += 1
            else:
                dict_1[item] = 1

    return sorted(dict_1.iteritems(), key=lambda asd:asd[1], reverse=True)
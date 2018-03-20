#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class xlsx_tag(object):

    def __init__(self,n,k):
        self.input = n
        self.out_put = k

    def read_xlsx(self):
        data = xlrd.open_workbook(self.input) # 打开xls文件
        table = data.sheets()[0] # 打开第一张表
        nrows = table.nrows # 获取表的行数
        list1 = []
        list2 = []
        list3 = []
        list_sentence = []
        dict = {}
        list_word = []
        for i in range(nrows): # 循环逐行打印
            if i == 0: # 跳过第一行
                continue
            list1.append(table.row_values(i)[:3][0]) # 取前一列
            list2.append(table.row_values(i)[:3][1]) #取前第二列
            list3.append(table.row_values(i)[:3][2])  # 取前第三列

        list_num1 = list1.__len__()
        #构建键值对,一个名字对应一个tag
        list_num2 = list2.__len__()
        for num in range(0,list_num2):
            print list2[num]
            l2  = list2[num].split("#")
            l3 = list3[num].split("#")
            tag_num = l2.__len__()
            for num2 in range(0,tag_num):
                dict[l2[num2]] = l3[num2]

        return list_num1,dict,list1,list2

    def get_tag(self):

        list_num1,dict,list1,list2 = self.read_xlsx()
        wf = open(self.out_put,"w+")

        #第一列的句子
        for num in range(0,list_num1):
            l2 = list2[num].split("#")
            dict_point = {}
            line = list1[num]
            sentence_len = len(line)
            print line
            for tag in l2:
                print tag
                for num3 in range(0,len(tag)):
                    #对应的 大 18 幂 19 幂 20
                    if(num3 == 0):
                        dict_point[line.index(tag ) + num3] = 'B-' + dict[tag]
                    elif(num3 == len(tag)-1):
                        dict_point[line.index(tag) + num3] = 'E-' + dict[tag]
                    else:
                        dict_point[line.index(tag) + num3] = 'M-' + dict[tag]

            for i in range(0,sentence_len):
                if(i in dict_point):
                    wf.write(line[i] + "\t")
                    wf.write(dict_point[i] + "\n")
                else:
                    wf.write(line[i]+"\t")
                    wf.write("W" + "\n")
            wf.write("\n")

        wf.close()

#输入的表格,输出的文档
p = xlsx_tag("1.xlsx","tag1.txt")
p.get_tag()


















# -*- coding: utf-8 -*-
from langconv import *
import os
import time
import xlrd
import sys
from langconv import *
reload(sys)
sys.setdefaultencoding('utf-8')


class bao(object):
    def tradition2simple(self,namelist):
        """
        将人名中的繁体字转换成简体字
        :param namelist:名字列表
        :return:结果列表
        """
        result = []
        for line in namelist:
            line = Converter('zh-hans').convert(line.decode('utf-8'))
            line = line.encode('utf-8')
            result.append(line)
            print 'test'
        return result


    def read_xlsx(self):
        data = xlrd.open_workbook("/home/gaorui/PycharmProjects/untitled3/标注/1/云峰标注集/既然青春留不住.xlsx")  # 打开xls文件
        table = data.sheets()[0]  # 打开第一张表
        nrows = table.nrows  # 获取表的行数
        list1 = []
        list2 = []
        list3 = []
        list_sentence = []
        dict = {}
        list_word = []
        for i in range(nrows):  # 循环逐行打印
            if i == 0:  # 跳过第一行
                continue
            # 进行繁体化简体
            list1.append(table.row_values(i)[:3][0])  # 取前一列

            list2.append(table.row_values(i)[:3][1])  # 取前第二列

            list3.append(table.row_values(i)[:3][2])  # 取前第三列
        return list1,list2,list3

    def fuckyou(self):
        list1,list2,list3 = self.read_xlsx()

        list5 = self.tradition2simple(list1)
        list4 = self.tradition2simple(list2)

        for i in range(0,list2.__len__()):
            print list5[i],list4[i]

p = bao()
p.fuckyou()


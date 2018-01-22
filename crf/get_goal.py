# -*- coding: utf-8 -*-

from __future__ import division

class get_reuslt_goal(object):
    def __init__(self, n):
        self.document = n

    def result_goal(self):
        #计算准确率
        sum = 0
        list1 = []
        list2 = []

        #我处理好的
        with open(self.document,"r") as p1:
            for i in p1.readlines():
                i = i.replace("\n","")
                if(i):
                    i = i.split("\t")

                    list1.append(i[i.__len__()-1])
                    if(i[i.__len__()-2] == i[i.__len__()-1]):
                        print i[i.__len__()-2],i[i.__len__()-1]
                        sum += 1
                    # print i[2]
                else:
                    continue
        print sum
        print "准确率为：　　"
        print sum/(list1.__len__())



#输出最终的准确率
v = get_reuslt_goal('3vali_result.txt')
v.result_goal()



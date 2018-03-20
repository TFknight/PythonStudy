# coding:utf-8
import jieba
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class text_class2(object):
    def __init__(self, n,k):
        self.input = n
        self.out_put = k

    #text1
    def get_text1(self):
        list = []
        result = []
        count = {}
        with open(self.input) as f:
            for i in f.readlines():
                i = i.replace('\n', '')
                i = i.split("	")
                k = i[0]
                if(k == "\n"):
                    continue
                else:
                    list.append(k)
        #初始化
        for k in list:
            count[k] = 0

        #统计单个字出现次数
        for i in list:
            count[i]+=1

        #对低频词进行更改
        kg = " "
        new_list = []
        for i in list:
            # if(count[i]<3):
            #     i = "❤"
            new_list.append(i + " ")
        # print kg.join(new_list)
        with open(self.out_put,"w+")as po:
            po.write("".join(new_list))
        print "write has done"

# coding:utf-8
import jieba
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class text_class(object):
    def __init__(self, n,k):
        self.input = n
        self.out_put = k

    #text1
    def get_text(self):
        list = []
        result = []
        count = {}
        with open(self.input) as f:
            for i in f.readlines():
                i.replace('\t', '').replace('\n', '')
                # print i
                i = i.split("	")
                k = i[0]
                list.append(k)
        #初始化
        for k in list:
            count[k] = 0

        #统计单个字出现次数
        for i in list:
            count[i]+=1

        #对低频词进行更改
        for i in list:
            if(count[i]<3):
                i = "❤"
            with open(self.out_put,"a")as po:
                po.write(i + " ")
        print "write has done"

    #text2
    def get_text2(self):
        list = []
        result = []
        count = {}
        with open(self.input) as f:
            for i in f.readlines():
                i.replace('\t', '').replace('\n', '')
                i = i.split(" ")
                for word in i:
                    list.append(word)

        # 初始化
        for k in list:
            count[k] = 0

        # 统计单个字出现次数
        for i in list:
            count[i] += 1

        # 对低频词进行更改
        for i in list:
            if (count[i] < 3):
                i = "❤"
            with open(self.out_put, "a")as po:
                po.write(i + " ")

        print "write has done"


# #在这里输入文档名字
# p = text_class("/home/gaorui/Downloads/trainPos.txt","baobao2.txt")
# #调用方法一
# p.get_text()
# #调用方法二
# p.get_text2()
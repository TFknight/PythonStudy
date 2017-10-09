# -*- coding: UTF-8 -*-
import os
import jieba


from pyltp import SentenceSplitter
#分句，也就是将一片文本分割为独立的句子
def sentence_splitter(sentence):
    sents = SentenceSplitter.split(sentence)  # 分句



l1 = []
allkey = []


try:
    # with open('/home/qistar/PycharmProjects/untitled1/trainSet.txt', 'r') as keywords:
    with open('/home/gaorui/PycharmProjects/untitled7/text/trainSet.txt', 'r') as keywords:
        for i in keywords.readlines():
            i=i.strip('\n')
            i=i.strip('\xef\xbb\xbf')
            k=i.split('')
            file=k[0]
            key=k[1:]
            allkey.extend(list(k[1:]))

            l2 = []
            text=[]

            try:
                # with open('/home/qistar/PycharmProjects/untitled1/Training_Blog/' + file + '.txt' , 'r') as e:
                with open('/home/gaorui/PycharmProjects/untitled7/Training_Blog/' + file + '.txt' , 'r') as e :
                    t = e.read()
                    listoftext = sentence_splitter(t)
                    for l in listoftext:
                        te = jieba.cut(l, cut_all=True)
                        text.extend(te)

                    text = list(set(text))
                    print type(text[0])
            finally:
                e.close()

            for b in text:
                    b = b.encode('utf-8')
                    l2.append(b)



            for k in key:
                if k in l2:
                    if k not in l1:
                        l1.append(k)

finally:
    keywords.close()


l4 = []
allkey=list(set(allkey))
l1=list(set(l1))
for k in allkey:
    if k not in l1:
        l4.append(k)





A=len(allkey)
B=len(l1)
C=len(l4)
D=float(B)/float(A)
print '共给出关键词：',A
print '分出关键词：',B
print '未能分出关键词：',C
print '召回率：',D

try:
    # with open('/home/qistar/PycharmProjects/untitled1/结巴测试结果.txt' , 'a') as po:
    with open('/home/gaorui/PycharmProjects/untitled7/结巴测试结果.txt' , 'a') as po:
        po.write('共有关键词：' )
        po.write(str(A))
        po.write('个')
        po.write('\n')
        po.write('已分出关键词：')
        po.write(str(B))
        po.write('个')
        po.write('\n')
        po.write('未能切出的关键词：')
        po.write(str(C))
        po.write('个')
        po.write('\n')
        po.write('jieba召回率：' )
        po.write( str(D))
        po.write('\n')
        po.write('未分出的词有：')
        po.write('\n')
        for op in l4:
            po.write( op )
            po.write( '\n' )
finally:
    po.close()



# import jieba
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))

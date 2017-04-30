#-*- coding:utf-8 -*-

import sys
reload(sys)
import codecs
import jieba
sys.setdefaultencoding( "utf-8" )


dict_pos_word = {}# 字典初始化
lines=""
items=[]

# 定义打开文件的方法
def getfile(path, charset='utf-8'):
    with open(path) as f:
        lines = [line.strip().decode(charset) for line in f.readlines()]#每次读取一行内容,默认删除空白符
    f.close()
    return lines

# 读取词典
pos_words = getfile('反派.txt')
for line in pos_words:
        line = line.strip('\n') # 删除换行符
        items.append((line, 0))#在列表中追加对象,更新现有的列表

#读取所有评论
article=getfile('太空旅客.txt')
for line in article:
    line.strip('\n')# 删除换行符
    lines+=line

#写入文档
file=open('result.txt','w')
itemsdict=dict(items)#返回一个完整的字典
words=jieba.cut(lines)#结巴分词

for word in words:
    if word in itemsdict.keys():#分词后的结果与该字典所有的键对比
        itemsdict[word]+=1

for k in itemsdict.keys():
    num=k+str(itemsdict[k])+'\n'
    file.write(num)




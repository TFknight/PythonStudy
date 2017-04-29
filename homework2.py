#-*- coding:utf-8 -*-

import sys
reload(sys)
import codecs
import jieba
sys.setdefaultencoding( "utf-8" )


dict_pos_word = {}
lines=""
items=[]

# 打开文件
def getfile(path, charset='utf-8'):
    with open(path) as f:
        lines = [line.strip().decode(charset) for line in f.readlines()]
    f.close()
    return lines

# 读取词典
pos_words = getfile('1.txt')
for line in pos_words:
        line = line.strip('\n')
        items.append((line, 0))

#读取所有评论
article=getfile('2.txt')
for line in article:
    line.strip('\n')
    lines+=line

#写入文档
file=open('3.txt','w')
itemsdict=dict(items)
words=jieba.cut(lines)

for word in words:
    if word in itemsdict.keys():
        itemsdict[word]+=1

for k in itemsdict.keys():
    num=k+str(itemsdict[k])+'\n'
    file.write(num)




# coding:utf-8
from get_text import text_class
import sys
import numpy
import  time
reload(sys)
sys.setdefaultencoding("utf-8")
from gensim.models import word2vec
from gensim.models import Word2Vec
import logging, gensim, os



def word_to_vec_method(document,dim_size,dim_count):

    word_bag = []
    sentences=word2vec.Text8Corpus(p.out_put)
    #设置最少出现次数为3
    model = Word2Vec(sentences, sg=1, size = dim_size,  window=5,  min_count=dim_count,  negative=3, sample=0.001, hs=1, workers=4)

    #加载和运行model
    model.save("model1")
    model = Word2Vec.load("model1")

    #去重
    for i in sentences:
        for word in i:
            word_bag.append(word)
    word_bag = set(word_bag)

    with open(document, "a")as po:
        po.write(str(word_bag.__len__()))
        po.write(" ")
        po.write(str(dim_size))
        po.write("\n")
        po.close()

    for k in word_bag:
        array = model[k]
        list_ar = array.tolist()
        print k,list_ar
        with open(document,"a")as pi:
            pi.write(k )
            pi.write(" ")
            for word_in in list_ar:
                pi.write(str(word_in))
                pi.write(" ")
            pi.write("\n")
    print "ok"


if __name__ == '__main__':
    # 在这里输入文档名字,输入文档 和 转换格式后的文档
    p = text_class("/home/gaorui/Downloads/trainPos.txt","baobao2.txt")
    # #调用方法一
    p.get_text()
    #输入要保存word2vec向量的文件路劲 和 向量的特征数
    word_to_vec_method("1.txt",100,3)



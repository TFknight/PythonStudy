# coding:utf-8
from get_text2 import text_class2
import sys
import numpy
import  time
reload(sys)
sys.setdefaultencoding("utf-8")
from gensim.models import word2vec
from gensim.models import Word2Vec
import logging, gensim, os


class CRF_word2vec(object):

    def __init__(self, n, j, k,m,l,h):
        self.vec_file = n
        self.dim_size = j
        self.dim_count = k
        self.vec_choice = m
        self.vali_file = l
        self.dif_output = h

    #训练w2v字向量
    def word_to_vec_method(self):
        word_bag = []
        word_dict = {}
        word_list = []
        tag_list = []

        #这里要分好一个个字去给word2vec做model
        sentences=word2vec.Text8Corpus(self.dif_output)

        #设置最少出现次数为3
        model = Word2Vec(sentences, sg=1, size = self.dim_size,  window=5,  min_count= self.dim_count,  negative=3, sample=0.001, hs=1, workers=4)

        #加载和运行model
        model.save("model")
        model = Word2Vec.load("model")
        print "model has ok"
        return sentences,model

    #取w2v的前n维做为特征
    def get_vec_num(self):
        weidu_dict = {}
        sentences,model = self.word_to_vec_method()
        # #去重
        for i in sentences:
            #每个句子的字组成的数列
            for word_num in range(0,i.__len__()):
                array = model[i[word_num]]
                list_ar = array.tolist()
                for i2 in range(0, list_ar.__len__()):
                    list_ar[i2] = str(list_ar[i2])

                #选多少维作为特征
                list_ar = list_ar[0:vec_choice]
                # list_ar = " ".join(list_ar)

                weidu_dict[i[word_num]] = list_ar
        return weidu_dict

    #写入文件
    def write_file(self,dif_input,dif_file):
        weidu_dict = self.get_vec_num()

        wf2 = open(dif_input, "r")
        wf2_list = wf2.readlines()
        wf2.close()

        po = open(dif_file, "w+")

        for line in wf2_list:
            if(line == "\n"):
                po.write("\n")
            else:
                try:
                    #输出格式有点奇怪不过是对的
                    line = line.split("\t")
                    line[0] = line[0].decode("utf-8")

                    print line[0],weidu_dict[line[0]],line[1]
                    po.write(line[0] + "    ")

                    str2 = ','.join(weidu_dict[line[0]])
                    po.write(str2 + "   ")

                    po.write(line[1])

                except:
                    pass

        po.close()

    def train_document(self):
        self.write_file(p1.input,self.vec_file)
        print "训练集已经完成"

    def vali_document(self):
        self.write_file(p2.input,self.vali_file)
        print "验证集已经完成"


if __name__ == '__main__':

    w2v_train_file = "3.txt"  #输入训练集　要保存word2vec向量的文件路劲
    vali_file = "3vali.txt"#输入验证集　要保存word2vec向量的文件路劲
    vec_num = 100  # 训练word２vec多少维
    min_count = 0  # 向量中最低出现单词个数
    vec_choice = 100  # 选多少维作为ＣＲＦ特征

    #训练集
    # 输入文档 和 转换格式后的文档
    p1 = text_class2("1.txt", "lab_tag.txt")
    p1.get_text1()
    p3 = CRF_word2vec(w2v_train_file, vec_num, min_count, vec_choice, vali_file,p1.out_put)
    p3.train_document()

    # 验证集
    p2 = text_class2("2.txt", "lab_tag2.txt")
    p2.get_text1()
    p4 = CRF_word2vec(w2v_train_file, vec_num, min_count, vec_choice, vali_file, p2.out_put)
    p4.vali_document()





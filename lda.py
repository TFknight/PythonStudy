#coding=utf-8
import jieba
import os
import numpy as np

from gensim import corpora, models,similarities
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

TRAINING_BLOG = '/home/gaorui/PycharmProjects/untitled8/lsi_try/yanzheng_seg1/'
TRAINING_USER_TAG = '/home/gaorui/PycharmProjects/untitled8/lsi_try/SMP-master/InterestModel/newdata/training.txt'
LABELSPACE = '/home/gaorui/PycharmProjects/untitled8/lsi_try/SMP-master/InterestModel/newdata/labelSpace.txt'

num_topics = 200

## 获得用户-标签空间
def get_user_tag_dict():
    user_tag_dict = {}
    f = open(TRAINING_USER_TAG)
    # f = open(VALIDATION_USER_TAG)
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        tokens = line.split(',')
        user = tokens[0]
        tag_list = [tokens[1],tokens[2],tokens[3]]
        user_tag_dict[user] = tag_list
        # print user, tag_list[0], tag_list[1], tag_list[2]
    return user_tag_dict
#{user1:[深度学习,机器学习,IT],user2:[移动开发,信息安全,web开发]}

## 获取标签空间
def get_labelSpace_dict():
    labelSpace_dict = {}
    f = open(LABELSPACE)
    lines = f.readlines()
    num = 0
    for line in lines:
        label = line.strip()
        if label not in labelSpace_dict:
            labelSpace_dict[label] = num
            # print label, labelSpace_dict[label]
            num += 1

    return labelSpace_dict
#深度学习:0,系统运维:1,项目管理:2

## 获得博客-标签空间
def get_blog_tag_dict():
    blog_tag_dict = {}
    user_tag_dict = get_user_tag_dict()
    labelSpace_dict = get_labelSpace_dict()
    for user in user_tag_dict:
        user_blogs_path = TRAINING_BLOG + user
        user_tag_list = user_tag_dict[user]
        user_tag_index_list = [labelSpace_dict[user_tag_list[0]],labelSpace_dict[user_tag_list[1]],labelSpace_dict[user_tag_list[2]]]
        if not os.path.exists(user_blogs_path):
            continue
        for path, dirs, files in os.walk(user_blogs_path):
            for blog in files:

                blog = blog.strip('.txt')
                tag_vector = [0 * i for i in range(0,42,1)]
                for index in user_tag_index_list:
                    tag_vector[index] += 1
                if blog not in blog_tag_dict:
                    blog_tag_dict[blog] = tag_vector
                else:
                    old_tag_vector = blog_tag_dict[blog]
                    for j in range(0,42,1):
                        old_tag_vector[j] += tag_vector[j]
                    blog_tag_dict[blog] = old_tag_vector

    return blog_tag_dict
## blog_tag_dict = {blog_id1:[0][1][2][3][4]...[200],blog_id2:[0][1][2]...[200]....}


## 获得博客的index标记,以及博客内容
def get_blog():
    blog_index_dict = {}
    blog_content_list = []
    blog_user_dict = {}
    index = 0
    user_tag_dict = get_user_tag_dict()
    for user in user_tag_dict:
        user_blogs_path = TRAINING_BLOG + user
        if not os.path.exists(user_blogs_path):
            continue
        for path, dirs, files in os.walk(user_blogs_path):
            for blog in files:
                blog_content_file = user_blogs_path + '/' + blog

                # 训练才用到博文内容
                f = open(blog_content_file)
                data = f.read().strip().lower().split('/')
                # print data
                print blog
                blog_content_list.append(data)

                blog = blog.strip('.txt')
                blog_index_dict[index] = blog
                index += 1
                blog_user_dict[blog] = user

    return blog_index_dict,blog_content_list, blog_user_dict

# 训练lda模型
def train_lda_model(blog_content_list):
    documents = blog_content_list   ## 每篇博客, 以及做好分词,去除无关标点符号
    texts = [[word for word in document] for document in documents] ## 将博客构建列表形式
    dictonary = corpora.Dictionary(texts)  ## 统计博客的出现的词项
    dictonary.save('/home/iiip/smp/task2/lda/dictionary.model')
    corpus = [dictonary.doc2bow(text) for text in texts]  ## 将博客转化为BOW形式
    tfidf = models.TfidfModel(corpus)  ## 提炼tfidf模型
    tfidf.save('/home/iiip/smp/task2/lda/tfidf.model')
    corpus_tfidf = tfidf[corpus]
    corpus_tfidf.save('/home/iiip/smp/task2/lda/corpus_tfidf.model')
    lda = models.LdaModel(corpus_tfidf, id2word=dictonary,num_topics=num_topics)  ## 训练lda模型, 隐式主题为num_topics
    lda.save('/home/iiip/smp/task2/lda/lda.model')
    corpus_lda = lda[corpus_tfidf]
    corpus_lda.save('/home/iiip/smp/task2/lda/corpus_lda.model')
    index = similarities.MatrixSimilarity(lda[corpus]) ## 用于计算博客相似度
    index.save('/home/iiip/smp/task2/lda/index.model')


traing_user_tag_dict = get_user_tag_dict()
blog_tag_dict = get_blog_tag_dict() ## 获得博客--标签映射表
blog_index_dict,blog_content_list, blog_user_dict = get_blog() ## 获取博客-id映射表，以及博客内容列表

train_lda_model(blog_content_list)
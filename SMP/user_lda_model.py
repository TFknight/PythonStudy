# coding=utf-8
from gensim import corpora, models
import os

## 读取字典
dictonary = corpora.Dictionary.load('/home/iiip/smp/task2/lda/dictionary.model')
## 读取lda模型
lda = models.LdaModel.load('/home/iiip/smp/task2/lda/lda.model')

## 训练集和验证集的路径
TRAINING_BLOG = '/home/iiip/smp/task2/lsi/Task2/output_seg/training_blog_seg/'
TRAINING_USER_TAG = '/home/iiip/smp/lsi_text/boss_code/Task2/newdata/training.txt'
LABELSPACE = '/home/iiip/smp/lsi_text/boss_code/Task2/newdata/labelSpace.txt'
VALIDATION_BLOG = '/home/iiip/smp/lsi_text/boss_code/Task2/newdata/validation_seg1/'
VALIDATION_USER_TAG = '/home/iiip/smp/lsi_text/boss_code/Task2/newdata/validation.txt'
TRAINING_BEHAVIOR = '/home/iiip/smp/lsi_text/boss_code/Task2/newdata/training_userBlog/'
VALIDATION_BEHAVIOR = '/home/iiip/smp/lsi_text/boss_code/Task2/newdata/vali_user_blog/'

# behavior_dict = { 0:0.4, 1:0.3, 2:0.2, 3:0.2, 4:0.1} # 0.418
# behavior_dict = { 0:0.5, 1:0.3, 2:0.2, 3:0.1, 4:0.1} 0.424
# behavior_dict = { 0:0.5, 1:0.3, 2:0.2, 3:0.2, 4:0.1} 0.436
# behavior_dict = { 0:0.4, 1:0.3, 2:0.2, 3:0.3, 4:0.1} 0.428
# behavior_dict = { 0:0.6, 1:0.3, 2:0.1, 3:0.2, 4:0.1} #0.434
# behavior_dict = { 0:1, 1:1, 2:1, 3:1, 4:1} 0.413
behavior_dict = { 0:0.6, 1:0.3, 2:0.2, 3:0.2, 4:0.1}
# 0.442
# behavior_dict = { 0:0.6, 1:0.2, 2:0.2, 3:0.3, 4:0.1} 0.433
# behavior_dict = { 0:0.6, 1:0.3, 2:0.2, 3:0.2, 4:0.1}

VECTOR_LENGTH = 200


import numpy as np
## 获取用户的lda模型平均向量
def create_user_lda_vector(user):
    user_vector = [0.0 * i for i in range(0,VECTOR_LENGTH,1)]
    # user_blogs_path = TRAINING_BLOG + user
    user_blogs_path = VALIDATION_BLOG + user
    # user_behavior_file =  TRAINING_BEHAVIOR + user + '.txt'
    user_behavior_file =  VALIDATION_BEHAVIOR + user + '.txt'
    f = open(user_behavior_file)
    lines = f.readlines()
    #lines就是用户行为的那几行东西　browse post
    blog_num = 0
    for path, dirs, files in os.walk(user_blogs_path):
        for blog in files:
            blog_content_file = user_blogs_path + '/' + blog
            blog_content = open(blog_content_file).read().lower().strip().split('/')
            query_bow = dictonary.doc2bow(blog_content)
            query_lda = lda[query_bow]
            beha = 0
            for t in range(0,lines.__len__(),1):
                if blog in lines[t]:
                    #如果blog在用户行为的那几行中出现，就返回这一行的行数t
                    beha = t
                    #有一个ｂｒｅａｋ就相当于一篇博客对应了一个用户行为，对应了一个权重
                    break
            blog_vector = [0.0 * i for i in range(0,VECTOR_LENGTH,1)]
            for j in range(0,len(query_lda),1):
                #200维随机找，确定这个博客的２００个权重分别是多少 （144,0.053224)
                i = query_lda[j]
                #beha表示在第几行的行为，第一行为post，第二行为favourite
                blog_vector[i[0]] = i[1] * behavior_dict[beha]## 增加对博客行为的权重
            blog_num += 1
            #两个矩阵叠加在一起，有的就有，没有的就为０
            user_vector = np.array(user_vector)+np.array(blog_vector)
    if blog_num == 0:
        #这个人读的博客有可能为全０篇
        user_vector = [0.0 * i for i in range(0, VECTOR_LENGTH, 1)]
        return user_vector
    #对这个人读过的博客进行平均
    user_vector = np.array(user_vector) / blog_num
    print user_vector
    return user_vector
# 每一篇博客*对应类型权重 之和/博客数量   即用户平均lda词向量



## 将向量写入文档中
def save_user_lda_vector(filename, vector_dict):
    f = open(filename, 'w')
    data = ''
    for user in vector_dict:
        line = user
        vector = vector_dict[user]
        for i in range(0, len(vector),1):
            line += ' ' + str(vector[i])
        data += line + '\n'
    f.write(data)
    print 'save is ok'
    f.close()

## 获得用户-标签空间
def get_user_tag_dict():
    user_tag_dict = {}
    # f = open(TRAINING_USER_TAG)
    f = open(VALIDATION_USER_TAG)
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        tokens = line.split(',')
        user = tokens[0]
        tag_list = [tokens[1],tokens[2],tokens[3]]
        user_tag_dict[user] = tag_list
        #{user:["jiqi","xuexi","haha"]}
        # print user, tag_list[0], tag_list[1], tag_list[2]
    return user_tag_dict

## 将训练集用户的lda保存
def save_user_vector():
    user_tag_dict = get_user_tag_dict()
    vector_dict = {}
    for user in user_tag_dict:
        # if not os.path.exists(TRAINING_BLOG + user):
        #     continue
        user_vector = create_user_lda_vector(user)
        vector_dict[user] = user_vector
    # file = 'train_lda.txt'
    file = '/home/iiip/smp/task2/lda/vali_lda.txt'
    save_user_lda_vector(file, vector_dict)


save_user_vector()

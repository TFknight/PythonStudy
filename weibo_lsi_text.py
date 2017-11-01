# coding=utf-8
from gensim import corpora, models
import os
import time

## 读取字典
dictonary = corpora.Dictionary.load('/home/iiip/DilicelSten/微博兴趣处理/result/result_model/dictionary.model')
## 读取lsi模型
lsi = models.LsiModel.load('/home/iiip/DilicelSten/微博兴趣处理/result/result_model/lsi.model')

## 训练集和验证集的路径
# TRAINING_BLOG = '../newdata/trainning_seg1/'
TRAINING_USER_TAG = '/home/iiip/DilicelSten/微博兴趣处理/result/user_tag.txt'
LABELSPACE = '/home/iiip/DilicelSten/微博兴趣处理/result/label.txt'
VALIDATION_BLOG = '/home/iiip/DilicelSten/微博兴趣处理/result/user_blog_seg/'#自己加
VALIDATION_USER_TAG = '/home/iiip/DilicelSten/微博兴趣处理/result/vali_tag.txt'
# TRAINING_BEHAVIOR = '../newdata/training_userBlog/'
# VALIDATION_BEHAVIOR = '../output_seg/output/pingce/'

# behavior_dict = { 0:0.4, 1:0.3, 2:0.2, 3:0.2, 4:0.1} 0.418
# behavior_dict = { 0:0.5, 1:0.3, 2:0.2, 3:0.1, 4:0.1} 0.424
# behavior_dict = { 0:0.5, 1:0.3, 2:0.2, 3:0.2, 4:0.1} 0.436
# behavior_dict = { 0:0.4, 1:0.3, 2:0.2, 3:0.3, 4:0.1} 0.428
# behavior_dict = { 0:0.6, 1:0.3, 2:0.1, 3:0.2, 4:0.1} 0.434
# behavior_dict = { 0:1, 1:1, 2:1, 3:1, 4:1} 0.413
# behavior_dict = { 0:0.6, 1:0.3, 2:0.2, 3:0.2, 4:0.1} 0.442
behavior_dict = { 0:0.7, 1:0.2, 2:0.2, 3:0.2, 4:0.1}#0.435

VECTOR_LENGTH = 200

## 获取用户的lsi模型平均向量
def create_user_lsi_vector(user):
    user_vector = [0.0 * i for i in range(0,VECTOR_LENGTH,1)]
    # user_blogs_path = TRAINING_BLOG + user
    user_blogs_path = VALIDATION_BLOG + user
    try:
        blog_content_file = user_blogs_path + ".txt"
        blog_content = open(blog_content_file).read().lower().strip().split('/')
        query_bow = dictonary.doc2bow(blog_content)
        query_lsi = lsi[query_bow]
        for j in range(0,VECTOR_LENGTH,1):
            user_vector[j] += query_lsi[j][1]  ## 增加对博客行为的权重
    except:
        for k in range(0, VECTOR_LENGTH, 1):
            user_vector[k] = 0
        return user_vector

    for k in range(0,VECTOR_LENGTH,1):
        user_vector[k] = user_vector[k]
    print user_vector
    return user_vector

## 将向量写入文档中
def save_user_lsi_vector(filename, vector_dict):
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
        tag_list = [tokens[1]]
        user_tag_dict[user] = tag_list
        # print user, tag_list[0], tag_list[1], tag_list[2]
    return user_tag_dict

## 将训练集用户的lsi保存
def save_user_vector():
    user_tag_dict = get_user_tag_dict()
    vali_user = open("/home/iiip/DilicelSten/微博兴趣处理/result/vali_user").read()
    vector_dict = {}
    for user in user_tag_dict:
        if user in vali_user:
            user_vector = create_user_lsi_vector(user)
            vector_dict[user] = user_vector
    # train_file = 'train_lsi.txt'
    file = '/home/iiip/DilicelSten/微博兴趣处理/result/result_model/vali.txt'
    save_user_lsi_vector(file, vector_dict)


save_user_vector()

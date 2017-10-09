# coding=utf-8
#全矩阵　ＳＶＣ
from sklearn.externals import joblib
import os
import jieba
import math

scorelist = []
#获取标签列表存为列表key，下标由１到４２
keys = []
try:
    with open('/home/qistar/PycharmProjects/untitled1/SMPCUP2017任务2训练集/SMPCUP2017_LabelSpace_Task2.txt', 'r') as Tag:
        for line in Tag.readlines():
            line = line.decode('GBK')
            line = line.strip('\n').strip("\r")
            keys.append(line)
finally:
    Tag.close()

# 获取　key为用户名，Value为对应用户的标签列表　的字典，下标有０到１０５５
DicUser = {}
try:
    with open('/media/qistar/DATA/SMP/SMPCUP2017_TrainingData_Task2.txt', 'r') as UserTag:
        # with open('/home/gaorui/PycharmProjects/untitled7/text/trainSet.txt', 'r') as keywords:
        for i in UserTag.readlines():
            i = i.strip('\n').decode('utf-8')
            i = i.strip('\r')
            k = i.split('')
            username = k[0]
            usertag = k[1:]
            DicUser[username] = usertag
finally:
    UserTag.close()




keytxt = os.listdir('/media/qistar/DATA/SMP/trainingDate_title/')

allword = set()
for kk in keytxt:
    #构建维度数量

    with open('/media/qistar/DATA/SMP/trainingDate_title/' + kk , 'r') as a:
       word = a.read()
       word = word.strip('\n')
       word = word.split(' ')
       for b in word:
           allword.add(b)

if '' in allword:
    allword.remove('')
allword = list(allword)


#向量初始化
xiangliang = []
for i in range(len(allword)):
    xiangliang.append(0)

#打开用户档案
key = []
keytxt = os.listdir('/media/qistar/DATA/SMP/TestDate_title/')
for k in keytxt:
    print k



    #获取标签
    user_Id = k.strip('.txt').decode('utf-8')


    for i in range(len(xiangliang)):
        xiangliang[i] = 0

    f = open('/media/qistar/DATA/SMP/TestDate_title/' + k, 'r')
    word = f.read()
    f.close()
    word = word.strip('\n')
    wordlists = word.split(' ')

    # 填写矩阵
    for i in wordlists:
        if i in allword:
            num = allword.index(i)
            xiangliang[num] = xiangliang[num] + 1

    print xiangliang
    user = []
    # 循环当前用户的４２个标签
    for i in range(42):
        # keynum = i + 1
        clf = joblib.load('/media/qistar/DATA/SMP/trr/model_' + str(i) + '.m')


        # 获取当前标签为１的概率
        result = clf.predict_proba(xiangliang)
        if i == 34 :
            present = float(result[0][1])
        elif i == 31 or i == 26 or i ==10 or i ==38 or i ==15:
            present = float(result[0][1])
        else:
            persent = math.sqrt(float(result[0][1]))*10

        user.append(persent)


    # 取前三名标签
    k = [[0, 0], [0, 0], [0, 0]]
    for i in range(len(user)):

        if user[i] >= k[0][1]:
            k.insert(0, [i, user[i]])
        elif user[i] >= k[1][1]:
            k.insert(1, [i, user[i]])
        elif user[i] >= k[2][1]:
            k.insert(2, [i, user[i]])

    score = 0
    for i in range(3):
        if keys[k[i][0]] in DicUser[user_Id]:
            score = score + 1
    score = float(score) / float(3)
    scorelist.append(score)

    # 为验证对比，按　用户名＋实际标签＋预测标签　写入txt
    with open('/media/qistar/DATA/SMP/第三次结果.txt', 'a') as pr:

        pr.write(user_Id.encode('utf-8'))
        pr.write(','.encode('utf-8'))
        pr.write(','.join(keys[k[i][0]]).encode('utf-8'))
        pr.write('\n'.encode('utf-8'))





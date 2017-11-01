# coding=utf-8

import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

## 读取训练数据
TRAINING_DATA = '/home/iiip/DilicelSten/微博兴趣处理/result/result_model/training.txt'
TRAINING_USER_TAG = '/home/iiip/DilicelSten/微博兴趣处理/result/training_tag.txt'
LABELSPACE = '/home/iiip/DilicelSten/微博兴趣处理/result/label.txt'
VALIDATION_BLOG = '/home/iiip/DilicelSten/微博兴趣处理/result/user_blog_seg/'#自己加
VALIDATION_USER_TAG = '/home/iiip/DilicelSten/微博兴趣处理/result/vali_tag.txt'
VALIDATE_DATA =  '/home/iiip/DilicelSten/微博兴趣处理/result/result_model/vali.txt'

## 获取标签空间
def get_labelSpace_dict():
    labelSpace_dict = {}
    label_list = []
    f = open(LABELSPACE)
    lines = f.readlines()
    num = 0
    for line in lines:
        label = line.strip()
        if label not in labelSpace_dict:
            labelSpace_dict[label] = num
            num += 1
            label_list.append(label)
    return labelSpace_dict, label_list


## 获得用户-标签空间
def get_training_user_tag_dict():
    user_tag_dict = {}
    f = open(TRAINING_USER_TAG)
    # f = open(VALIDATION_USER_TAG)
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        tokens = line.split(',')
        user = tokens[0]
        tag_list = [tokens[1]]
        user_tag_dict[user] = tag_list
        # print user, tag_list[0], tag_list[1], tag_list[2]
    return user_tag_dict

## 获得用户-标签空间
def get_vali_user_tag_dict():
    user_tag_dict = {}
    f = open(VALIDATION_USER_TAG)
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        tokens = line.split(',')
        user = tokens[0]
        tag_list = [tokens[1]]
        user_tag_dict[user] = tag_list
    return user_tag_dict

labelSpace_dict, label_list = get_labelSpace_dict()
training_user_tag_dict = get_training_user_tag_dict()
vali_user_tag_dict = get_vali_user_tag_dict()

## 将标签转化为向量空间
def label_to_vector(user):
    label_vector = [0 * i for i in range(0,24,1)]
    user_label = training_user_tag_dict[user]
    for label in user_label:
        j = labelSpace_dict[label]
        label_vector[j] = 1
    return label_vector


def load_training_data():
    f = open(TRAINING_DATA)
    lines = f.readlines()
    X = []
    y = []
    for line in lines:
        line = line.strip()
        tokens = line.split(" ")
        user = tokens[0]
        features = tokens[1:]
        for i in range(0,features.__len__(),1):
            features[i] = float(features[i])
        labels = training_user_tag_dict[user]
        for label in labels:
            X.append(features)
            y.append(labelSpace_dict[label])
    return X, y

def load_data():
    f = open(VALIDATE_DATA)
    lines = f.readlines()
    X = []
    y = []
    for line in lines:
        line = line.strip()
        tokens = line.split(" ")
        user = tokens[0]
        features = tokens[1:]
        for i in range(0,features.__len__(),1):
            features[i] = float(features[i])
        labels = vali_user_tag_dict[user]
        label_y = []
        for label in labels:
            label_y.append(labelSpace_dict[label])
        X.append(features)
        y.append(label_y)
    return X, y


from sklearn.model_selection import ShuffleSplit
from sklearn.linear_model import LogisticRegression
import numpy as np

feature_num = 200

def train_model(label):

    label_index = labelSpace_dict[label]
    X, y = load_training_data()

    ## 将数据平均分成10份,9份用作训练,预测属性为二元属性
    rs = ShuffleSplit(n_splits=10, test_size=.1, random_state=0)
    rs.get_n_splits(X)
    X_Fold = []
    y_Fold = []
    for train_index, test_index in rs.split(X):
        x_train = []
        y_train = []
        for i in train_index:
            x_train.append(X[i])
            if y[i] == label_index:
                y_train.append(1)
            else:
                y_train.append(0)
        X_Fold.append(x_train)
        y_Fold.append(y_train)

    logre_classifier = []
    ## 训练是10个二元分类模型
    for i in range(0,X_Fold.__len__(),1):
        classifier = LogisticRegression()
        classifier.fit(X_Fold[i],y_Fold[i])
        logre_classifier.append(classifier)
    # print logre_classifier.__len__()
    return logre_classifier

def step_first_classfier():
    classfiers_dict = {}
    for label in labelSpace_dict:
        print label, labelSpace_dict[label]
        logre_classifier = train_model(label)
        classfiers_dict[label] = logre_classifier
    return classfiers_dict

def step_first_train(classfiers_dict):

    ## 将数据分成1份训练
    X, y = load_training_data()



    rs = ShuffleSplit(n_splits=1, test_size=.1, random_state=0)
    rs.get_n_splits(X)
    x_train = []
    y_train = []
    X_test = []
    y_test = []
    for train_index, test_index in rs.split(X):
        for i in train_index:
            x_train.append(X[i])
            y_train.append(y[i])
        for i in test_index:
            X_test.append(X[i])
            y_test.append(y[i])

    step1_X = x_train
    step1_y = y_train

    ## 对每个类别作概率预测
    new_X = []
    for i in range(0, step1_X.__len__(), 1):
        pro_X = [0 * j for j in range(0,24,1)]
        for label in labelSpace_dict:
            label_index = labelSpace_dict[label]
            pro_total = 0.0
            logre_classifier = classfiers_dict[label]
            for t in range(0, logre_classifier.__len__(),1):
                clf = logre_classifier[t]
                # print step1_X[i]
                pro = clf.predict_proba(step1_X[i])
                # print pro[0][1]
                pro_total += pro[0][1]
            pro_total = pro_total / logre_classifier.__len__()
            pro_X[label_index] = pro_total
        # print pro_X
        new_X.append(pro_X)

    return new_X, step1_y

from sklearn.ensemble import RandomForestClassifier


# def step_two_train(new_X,step1_y):
#     classify_model = RandomForestClassifier(n_estimators=2000, random_state=1)
#     classify_model.fit(new_X, step1_y)
#     return classify_model


from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.utils import np_utils

## one_hot映射
def one_hot_encode_object_array(arr):
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))

def step_two_train(X, y):  ## X为特征向量, y为目标属性

    train_y_ohe = one_hot_encode_object_array(y)
    model = Sequential()
    model.add(Dense(60, input_shape=(200,)))
    model.add(Activation('sigmoid'))
    # model.add(Dropout(0.02))  ## 避免过拟合
    model.add(Dense(24))
    model.add(Activation('softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
    model.fit(X, train_y_ohe, nb_epoch=100, batch_size=1, verbose=1,validation_split=0.1)
    #交叉校验 validation_split = 0.1
    return model




def step_one_predict(X_test):
    ## 对每个类别作概率预测
    new_X = []
    for i in range(0, X_test.__len__(), 1):
        pro_X = [0 * j for j in range(0, 24, 1)]
        for label in labelSpace_dict:
            label_index = labelSpace_dict[label]
            pro_total = 0.0
            logre_classifier = classfiers_dict[label]
            for t in range(0, logre_classifier.__len__(), 1):
                clf = logre_classifier[t]
                # print step1_X[i]
                pro = clf.predict_proba(X_test[i])
                # print pro[0][1]
                pro_total += pro[0][1]
            pro_total = pro_total / logre_classifier.__len__()
            pro_X[label_index] = pro_total
        # print pro_X
        new_X.append(pro_X)
    return new_X


def step_two_predict(X, model):
    predict_y = []
    result = model.predict_proba(X) ## 预测概率
    for i in range(0,result.__len__(), 1):
        result[i] = np.array(result[i])
        topk = result[i][np.argpartition(result[i],-1)[-1:]] ## 取概率最大的前三个标签
        print topk
        predict = []
        for j in range(0,24,1):
            if result[i][j] in topk:
                predict.append(j)
        predict_y.append(predict)
    return predict_y


# classfiers_dict = step_first_classfier()
# new_X, step1_y = step_first_train(classfiers_dict)

X, y = load_training_data()
new_X, step1_y = X, y
step2_model = step_two_train(new_X,step1_y)


X_test, y_test = load_data()
step1_X = X_test
# step1_X = step_one_predict(X_test)
predict_y = step_two_predict(step1_X,step2_model)
precision = 0.0
num = 0
for i in range(0,y_test.__len__()):
    #取概率最大的第一个
    print y_test[i], predict_y[i],predict_y[i][0]
    n = predict_y[i][0]
    list_try = []
    list_try.append(n)
    list_inter = list(set(y_test[i]).intersection(set(list_try)))
    precision += 1.0 * list_inter.__len__() /1
    num += 1

print num
print precision / y_test.__len__()

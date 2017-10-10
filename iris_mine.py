#coding=utf-8
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# Generate dummy data
import numpy as np
#
# from __future__ import  print_function
from keras.models import Sequential
from sklearn.datasets import load_iris
from keras.layers.core import Dense,Dropout,Activation
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
import numpy as np
import csv
import pandas

## one_hot映射
def one_hot_encode_object_array(arr):
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))

def network_train(X, y):  ## X为特征向量, y为目标属性

    train_y_ohe = one_hot_encode_object_array(y)
    model = Sequential()
    model.add(Dense(200, input_shape=(4,)))
    model.add(Activation('sigmoid'))
    # model.add(Dropout(0.02))  ## 避免过拟合
    model.add(Dense(3))
    model.add(Activation('softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
    model.fit(X, train_y_ohe, nb_epoch=100, batch_size=1, verbose=1)
    return model


#训练数据特征标签分离
#转换为矩阵,并对数据类型进行转化,转化为float数据类型
X, y = load_iris()['data'], load_iris()['target']

#
from sklearn.model_selection import ShuffleSplit
rs = ShuffleSplit(n_splits=1, train_size=0.6, test_size=0.4, random_state=0)
rs.get_n_splits(X)
X_trainset = None
X_testset = None
y_trainset = None
y_testset = None

for train_index, test_index in rs.split(X, y):
    X_trainset, X_testset = X[train_index], X[test_index]
    y_trainset, y_testset = y[train_index], y[test_index]


model = network_train(X_trainset, y_trainset)
result = model.predict(X_testset)
test_y_ohe = one_hot_encode_object_array(y_testset)

loss, accuracy = model.evaluate(X_testset,test_y_ohe,verbose=0)
print ("Accuracy = {:.2f}".format(accuracy))
# print result
#
# predict_y = model.predict_proba(test_X)
#


# loss, accuracy = model.evaluate(X_testset,y_set,verbose=0)
# print ("Accuracy = {:.2f}".format(accuracy))
#
#
#
#
# trainData = np.array(load_iris())
# # print trainData
# X = trainData.data
# Y = trainData.target
# print X
# print Y
# # print trainData.shape
# trainDataFeature = trainData[:,:4].astype(float)
# trainDataLabel = trainData[:,4:].astype(float)
# # print trainDataFeature[0]
# #将标签进行编码，one-hot编码
#
# ## one_hot映射
# # def one_hot_encode_object_array(arr):
# #     uniques, ids = np.unique(arr, return_inverse=True)
# #     return np_utils.to_categorical(ids, len(uniques))
# #
# # trainLabeled = one_hot_encode_object_array(trainDataLabel)
#
# encoder = LabelEncoder()
# encoded_label = encoder.fit_transform(trainDataLabel[1])
#
# trainLabeled = np_utils.to_categorical(encoded_label)
# print trainLabeled
# # print trainLabeled.shape
#
# #搭建网络架构
# model = Sequential()
# # model.add(Dense(60, input_shape=(150,)))
# model.add(Dense(units=200,kernel_initializer='uniform',input_dim=4))
# model.add(Activation('sigmoid'))
# model.add(Dropout(0.02))  ## 避免过拟合
# model.add(Dense(42))
# model.add(Activation('softmax'))
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
#
# #数据训练
# model.fit(trainDataFeature[0:2],trainLabeled, nb_epoch=100, batch_size=1)
# # print model.evaluate(trainDataFeature,trainLabeled)

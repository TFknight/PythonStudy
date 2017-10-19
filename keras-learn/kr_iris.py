## coding=utf-8

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

def one_hot_encode_object_array(arr):
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))


iris = sns.load_dataset("iris")
# print iris
# print "*"*100
X = iris.values[:, :4]
y = iris.values[:, 4]
# print y

train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.6, random_state=0)
train_y_ohe = one_hot_encode_object_array(train_y)
test_y_ohe = one_hot_encode_object_array(test_y)

# Encoder = Sequential([Dense(8, input_dim=4), Activation('sigmoid')])
# Decoder = Sequential([Dense(4, input_dim=8), Activation('sigmoid')])

model = Sequential()
# model.add(Encoder)
# model.add(Decoder)
model.add(Dense(200,input_shape=(4,)))
model.add(Activation('relu'))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
model.fit(train_X, train_y_ohe, nb_epoch=100, batch_size=1, verbose=1)

# predict_y = model.predict_proba(test_X)
# print predict_y

loss, accuracy = model.evaluate(test_X,test_y_ohe,verbose=0)
print ("Accuracy = {:.2f}".format(accuracy))
# print
# print predict_y[0][0]

# # -*- coding: UTF-8 -*-
# #freedonforest
#
#
# import random
# from sklearn.externals import joblib
# from sklearn import svm
# from sklearn.datasets import load_svmlight_file
# from sklearn import cross_validation
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import MultiLabelBinarizer
# from sklearn.preprocessing import LabelBinarizer
# import numpy as np
# import pickle
#
# filenameX = "/media/qistar/DATA/SMP/X2.txt"
# data = load_svmlight_file(filenameX)
# X, Y = data[0], data[1]
#
# X = X.toarray()
# # Y = Y.toarray()
#
#
#
#
# X_train = []
# X_test = []
# Y_train = []
# Y_test = []
#
# rs = cross_validation.ShuffleSplit(len(Y), n_iter=1,  train_size=0.7,test_size=0.3, random_state=1)
#
# for train_index, test_index in rs:
#     train = train_index
#     test = test_index
#
# for tra in train:
#     X_train.append(X[tra])
#     Y_train.append(Y[tra])
#
# for te in test:
#     X_test.append(X[te])
#     Y_test.append(Y[te])
#
#
#
# # Y_train =MultiLabelBinarizer().fit_transform(Y_train)
#
# clf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#             max_depth=None, max_features='auto', max_leaf_nodes=None,
#             min_impurity_split=1e-07, min_samples_leaf=1,
#             min_samples_split=2, min_weight_fraction_leaf=0.0,
#             n_estimators=100, n_jobs=1, oob_score=False, random_state=None,
#             verbose=0, warm_start=False)
# clf.fit(X_train,Y_train)
# result = clf.predict(X_test)
# result2 = clf.predict_proba(X_test)
#
# print result
# print Y_test
#
#
# score = 0
# with open('/media/qistar/DATA/SMP/randonforest2.txt' , 'a') as resu:
#     for num in range(len(Y_test)):
#
#         resu.write(    str(    Y_test[num]    ).encode('utf-8')    )
#         resu.write('\n'.encode('utf-8'))
#
#
#         resu.write(    str(    result[num]    ).encode('utf-8')   )
#         resu.write('\n'.encode('utf-8'))
#
#
#         resu.write(    str(    result2[num]    ).encode('utf-8')    )
#         resu.write('\n'.encode('utf-8'))
#
#
#         resu.write('-'*100)
#         resu.write('\n'.encode('utf-8'))
#
#
#
#
#         if result[num] == Y_test[num]:
#             score = score +1
#
#
# score = float(score)/len(Y_test)
# print score
#
# with open('/media/qistar/DATA/SMP/randonforest2.txt' , 'a') as resu:
#     resu.write(str(score).encode('utf-8'))



# -*- coding: UTF-8 -*-
#　ＳＶＣ


from sklearn import svm
from sklearn.datasets import load_svmlight_file
from sklearn import cross_validation

filenameX = "/media/qistar/DATA/SMP/X2.txt"
data = load_svmlight_file(filenameX)
X, Y = data[0], data[1]

X = X.toarray()





X_train = []
X_test = []
Y_train = []
Y_test = []

rs = cross_validation.ShuffleSplit(len(Y), n_iter=1,  train_size=0.7,test_size=0.3, random_state=1)

for train_index, test_index in rs:
    train = train_index
    test = test_index

for tra in train:
    X_train.append(X[tra])
    Y_train.append(Y[tra])

for te in test:
    X_test.append(X[te])
    Y_test.append(Y[te])


print 'load OK'
# Y_train =MultiLabelBinarizer().fit_transform(Y_train)

clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
              decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
              max_iter=-1, probability=True, random_state=None, shrinking=True,
              tol=0.001, verbose=False)
clf.fit(X_train,Y_train)
result = clf.predict(X_test)
result2 = clf.predict_proba(X_test)

print 'fit OK'


present = []


print result
print result2
print Y_test


score = 0
with open('/media/qistar/DATA/SMP/SVM2.txt' , 'a') as resu:
    for num in range(len(Y_test)):

        resu.write(    str(    Y_test[num]    ).encode('utf-8')    )
        resu.write('\n'.encode('utf-8'))


        resu.write(    str(    result[num]    ).encode('utf-8')   )
        resu.write('\n'.encode('utf-8'))


        resu.write(    str(    result2[num]    ).encode('utf-8')    )
        resu.write('\n'.encode('utf-8'))


        resu.write('-'*100)
        resu.write('\n'.encode('utf-8'))




        if result[num] == Y_test[num]:
            score = score +1


score = float(score)/len(Y_test)
print score

with open('/media/qistar/DATA/SMP/SVM2.txt' , 'a') as resu:
    resu.write(str(score).encode('utf-8'))
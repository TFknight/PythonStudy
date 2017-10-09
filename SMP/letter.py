# coding=utf-8
import os
import jieba
import sys
from fractions import Fraction

reload(sys)

sys.setdefaultencoding('utf-8')
id_list = []
connext = {}
connext2 = {}
def getFollow(user_id):
    follow_dict = {}
    follow_dict[user_id] = []
    with open('/home/gaorui/PycharmProjects/untitled7/9_Letter.txt', 'r') as keywords:
        for line in keywords.readlines():
            line = line.strip('\n').strip("\r")
            tokens = line.split('')
            follow = tokens[0]
            user = tokens[1]
            if user == user_id:
                follow_dict[user_id].append(follow)
    return follow_dict

def getFollow2(user_id):
    follow_dict2 = {}
    follow_dict2[user_id] = []
    with open('/home/gaorui/PycharmProjects/untitled7/9_Letter.txt', 'r') as keywords:
        for line in keywords.readlines():
            line = line.strip('\n').strip("\r")
            tokens = line.split('')
            follow = tokens[1]
            user = tokens[0]
            if user == user_id:
                follow_dict2[user_id].append(follow)
    return follow_dict2


def main():
    user_id = raw_input("input you need:")
    user_id = user_id.strip('\n')
    follow_dict = getFollow(user_id)
    follow_dict2 = getFollow2(user_id)
    print "和他联系的发送者："
    print follow_dict[user_id]
    myset1 = set(follow_dict[user_id])
    for item1 in myset1:
        connext[item1] = follow_dict[user_id].count(item1)
    print connext

    print "和他联系的接受者"
    print follow_dict2[user_id]
    myset2 = set(follow_dict2[user_id])
    for item2 in myset2:
        connext2[item2] = follow_dict2[user_id].count(item2)
    print connext2

main()

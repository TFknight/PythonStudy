# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    Dir = {}
    allbacklist = []

    try:
        with open('/home/qistar/PycharmProjects/untitled1/8_Follow.txt', 'r') as keywords:
            for line in keywords.readlines():
                line = line.strip('\xef\xbb\xbf')
                line = line.strip('\n').strip("\r")
                Number = line.split('')
                back = Number[1]
                allbacklist.append(back)
    finally:
        keywords.close()

    backlist = set(allbacklist)
    for i in backlist:
        Dir[i] = []

    try:
        with open('/home/qistar/PycharmProjects/untitled1/8_Follow.txt', 'r') as keywords:
            for line in keywords.readlines():
                line = line.strip('\n').strip("\r")
                Number = line.split('')
                head = Number[0]
                back = Number[1]
                if head not in Dir[back]:
                    Dir[back].append(head)
    finally:
        keywords.close()

    user_id = raw_input('输入Number:')
    print user_id + '关注的人有：'
    print Dir[user_id]
    print '-' * 1000

    ResultDir = {}
    for user2_id in allbacklist:
        if user_id == user2_id:
            pass
        else:
            x1 = len(Dir[user_id])
            x2 = len(Dir[user2_id])
            x3 = len(set(Dir[user_id] + Dir[user2_id]))
            x = x1 + x2 - x3
            if x != 0:
                ResultDir[user2_id] = x
    print user_id + '的RAR关系有：'
    print ResultDir


main()
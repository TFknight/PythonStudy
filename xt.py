# -*- coding: UTF-8 -*-
import letter2
import follower2
import GetBlog

#获取标签列表
key = []
DicTag = {}
try:
    with open('/home/qistar/PycharmProjects/untitled1/SMPCUP2017任务2训练集/SMPCUP2017_LabelSpace_Task2.txt', 'r') as Tag:
        for line in Tag.readlines():
            line = line.decode('GBK')
            line = line.strip('\xef\xbb\xbf')
            line = line.strip('\n').strip("\r")
            key.append(line)
            DicTag[line] = {  u'PRAR':0  }

finally:
    Tag.close()



#获取　key为用户名，Value为对应用户的标签列表　的字典，下标有０到１０５５
DicUser = {}
try:
    with open('/home/qistar/PycharmProjects/untitled1/SMPCUP2017任务2训练集/SMPCUP2017_TrainingData_Task2.txt', 'r') as UserTag:
    # with open('/home/gaorui/PycharmProjects/untitled7/text/trainSet.txt', 'r') as keywords:
        for i in UserTag.readlines():
            i=i.strip('\n').decode('utf-8')
            i=i.strip('\xef\xbb\xbf').strip('\r')
            k=i.split('')
            username=k[0]
            usertag=k[1:]
            DicUser[username] = usertag
finally:
    UserTag.close()




for us in DicUser:
    user_id = us
    print user_id

    PRAR = follower2.getRAR(user_id)




    for i in PRAR:
        try:
            for j in DicUser[i]:
                DicTag[j][u'PRAR'] = DicTag[j][u'PRAR'] + PRAR[i]
        except:
            pass

    try:
        with open('/home/qistar/PycharmProjects/untitled1/L&F/Result/' + user_id + '.txt', 'a') as file:
            file.write( ' '.join( DicUser[user_id] ) )
            file.write( '\n' )

            for us in key:


                file.write(str(DicTag[us][u'PRAR']))
                file.write(u' ')


                file.write(u'\n')

    finally:
        file.close()




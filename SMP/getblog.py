# -*- coding: UTF-8 -*-
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os.path

print "OK"


ID_add = []
title_add = []
content_add = []
for i in os.listdir("/home/iiip/SMP/training_blog"):
        i = i.strip(".txt")
        if "idea" in i :
            continue
        try:
            with open("/home/iiip/SMP/training_blog/" + i + ".txt") as Blog:
                user_line = Blog.readlines()
                BRBA = []
                total_seg = ''  ## 记录用户的所有博客内容和标题
                for j in range(len(user_line)):
                    print user_line[j]
                    BRBA1 = user_line[j]
                    BRBA1 = BRBA1.strip('\n')
                    id_list = re.findall('u\'(.*?)\'', BRBA1)
                    analyse_result = []
                    for id in id_list:
                        if "D" in id:
                            print id
                            get1 = int(id.strip("D"))
                            get2 = (get1 - 1) / 5000
                            get_down = get2 * 5000 + 1
                            get_up = (get2 + 1) * 5000
                            if get_up > 895000:
                                continue
                            s_down = "%07d" % get_down
                            s_up = "%07d" % get_up
                            dir_down = 'D' + s_down
                            dir_up = 'D' + s_up
                            with open("/home/iiip/桌面/Corpus/" + dir_down + "-" + dir_up + "/" + id + ".txt",
                                      "r") as articles:
                                article = articles.readlines()

                                with open("/home/iiip/SMP/training_document/" + i + ".txt","w") as po:
                                        po.write(article)
                                        po.close()
        except:
            continue



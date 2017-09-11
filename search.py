#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.index import create_in
from whoosh.index import open_dir
from jieba.analyse import ChineseAnalyzer
# from pyltp import Segmentor
analyzer = ChineseAnalyzer()
import os.path
# import pyltp
filename_list=[]
ID_list = []
schema = Schema(title=TEXT, content=TEXT)

schema = Schema(title=TEXT(stored=True, analyzer=analyzer), content=TEXT(stored=True, analyzer=analyzer),
                 ID=ID(stored=True),tags=KEYWORD, icon=STORED, )

path_generator = os.walk("./blog_engine")
for path,d,filelist in path_generator:
    for filename in d:

        ix = open_dir("/home/iiip/桌面/blog_engine/" + filename)

        try:
            result_add = []
            result_str = []
            key_add = []
            ID_add = []
            dict_pos_word = {}
            searcher = ix.searcher()
            # with open('/home/iiip/桌面/search4000/2017text.txt', 'r') as keywords:
            #     for i in keywords.readlines():
            #         ID_add = []
            #         i = i.strip('\n')
            #         # searcher = ix.searcher()
            #         search_str = unicode(i)
            search_str = u"虚拟现实"
            results = searcher.find("title",search_str)
            # print len(results)
            # if not os.path.exists("/home/iiip/桌面/" + search_str):
            #     os.mkdir("/home/iiip/桌面/" + search_str)
            for hit in results:
                if hit.score > 0:
                    if len(ID_add) <= 20:
                        print search_str
                        ID_add.append(hit['ID'])
                        print hit['ID']
                        print hit.score
                        print "-" * 50
                        hit['ID'].encode('utf-8')
                        # i.encode('utf-8')
                        a = "/home/iiip/桌面/虚拟现实/" + hit['ID'] + ".txt"

                        with open(str(a),'w') as po:
                            po.write(hit['ID'])
                            po.write("\n")
                            po.write(hit['title'])
                            po.write("\n")
                            po.write(hit['content'])


        finally:
            searcher.close()
#coding=utf-8

__author__ = 'root'

# from extract import extract
import os
import jieba
import math
import codecs
import pickle
class Chiextration:


    categories = [u'web开发',u'并行及分布式计算',u'大数据技术',u'地理信息系统',u'电子商务',u'多媒体处理',u'机器人',u'机器学习',u'计算机辅助工程',u'计算机视觉',u'企业信息化',u'嵌入式开发',u'人工智能',u'人机交互',u'人脸识别',u'软件工程',u'商业智能',u'深度学习',u'数据恢复',u'数据可视化',u'数据库',u'数据挖掘',u'算法',u'图像处理',u'推荐系统',u'网络管理与维护',u'网络与通信',u'文字识别',u'物联网',u'系统运维',u'项目管理',u'信息安全',u'虚拟化',u'虚拟现实',u'移动开发',u'硬件',u'游戏开发',u'语音识别',u'云计算',u'增强现实',u'桌面开发',u'自然语言处理']

    def __init__(self, document):
        self.document = {}
        self.document = document
        self.docNum = self.DocNum()
        self.cateinDoc = self.CountCategory()
        self.wordlist = self.Getwordlist()

    def CountCategory(self):##统计文档中每个类别的数目
        cateinDoc = {}
        for category in Chiextration.categories:
            number = self.CateInDoc(category)
            cateinDoc[category] = number
        return cateinDoc

    def WordInDoc(self, word):##计算单词在所有文档中的频数
        count = 0
        for content in self.document:
            if word in content:
                count += 1
        return count

    def CateInDoc(self, category): ##计算类别在文档中的数目
        categories = self.document.values()
        return categories.count(category)

    def DocNum(self): ##计算文档数目
        return self.document.__len__()

    def WordInCate(self, word, category):##计算词语在所属类别文档中的频数(不含重复)
        count = 0
        for doc in self.document:
            if self.document[doc] == category:
                if word in doc:
                    count += 1
        return count

    def CalculateCHI(self, word, category):##计算卡方统计的值
        docNum = self.docNum
        wordInDoc = self.WordInDoc(word) #A+B
        wordNotInDoc = docNum - wordInDoc #C+D
        cateIndoc = self.cateinDoc[category] #A+C
        cateNotIndoc = docNum - cateIndoc #B+D
        wordInCate = self.WordInCate(word, category) #A
        wordNotInCate = wordInDoc - wordInCate #B
        cateWithoutWord = cateIndoc - wordInCate #C
        notCateAndWord = wordNotInDoc - wordNotInCate #D
        N = docNum * float(wordInCate*notCateAndWord-wordNotInCate*cateWithoutWord) * (wordInCate*notCateAndWord-wordNotInCate*cateWithoutWord)
        M = (cateIndoc+0.1) * (wordInDoc+0.1) * (cateNotIndoc+0.1) * (wordNotInDoc+0.1)
        chi = float(N) / M
        return chi

    def Getwordlist(self):##得到所有文档的词语集合
        wordlist = []
        for doc in self.document:
            words = doc.split(',')
            for word in words:
                wordlist.append(word)
        return wordlist

    def wordfrequent(self, word, category):##计算词语在所属类别文档中的频数(含重复)
        wordlist = self.wordlist
        cateInDoc = self.CateInDoc(category)
        frequent = float(wordlist.count(word))/(cateInDoc+1)
        return frequent


    def ImproCalculateCHI(self, word, category): ##改进后的chi,融合了frequency和tfidf
        docNum = self.docNum
        wordInCate = self.WordInCate(word, category) #A
        cateIndoc = self.cateinDoc[category] #A+C
        wordInDoc = self.WordInDoc(word) #A+B
        wordNotInDoc = docNum - wordInDoc #C+D
        cateNotIndoc = docNum - cateIndoc #B+D
        wordNotInCate = wordInDoc - wordInCate #B
        cateWithoutWord = cateIndoc - wordInCate #C
        notCateAndWord = wordNotInDoc - wordNotInCate #D
        wordlist = self.wordlist
        if (wordInCate*notCateAndWord-wordNotInCate*cateWithoutWord) <= 0:
            return 0
        tf = float(wordlist.count(word)) / wordlist.__len__()
        if tf == 0:
            return 0
        idf = math.log(float(self.document.__len__())/(wordInDoc+0.1))
        tfidf = tf * idf
        N = docNum * float(wordInCate*notCateAndWord-wordNotInCate*cateWithoutWord) * (wordInCate*notCateAndWord-wordNotInCate*cateWithoutWord)
        M = (cateIndoc+0.1) * (wordInDoc+0.1) * (cateNotIndoc+0.1) * (wordNotInDoc+0.1)
        chi = float(N) / M
        frequent = self.wordfrequent(word, category)
        chi *= frequent * tfidf
        return chi



def SplitWord(sentences): ##分词并去除停用词和单个词
    stopwordfile = open('../工具/哈工大停用词表.txt','r')
    data = stopwordfile.readlines()
    stopwords = []
    for word in data:
        stopwords.append(word)
    words = jieba.cut_for_search(sentences)
    wordlist = []
    for word in words:
        wordlist.append(word)
    words =[]
    for word in wordlist:
        if word.__len__() >= 2 and word.encode('utf-8') not in stopwords:
            words.append(word)
    return words


class Feature_selection:
    categories = [u'web开发',u'并行及分布式计算',u'大数据技术',u'地理信息系统',u'电子商务',u'多媒体处理',u'机器人',u'机器学习',u'计算机辅助工程',u'计算机视觉',u'企业信息化',u'嵌入式开发',u'人工智能',u'人机交互',u'人脸识别',u'软件工程',u'商业智能',u'深度学习',u'数据恢复',u'数据可视化',u'数据库',u'数据挖掘',u'算法',u'图像处理',u'推荐系统',u'网络管理与维护',u'网络与通信',u'文字识别',u'物联网',u'系统运维',u'项目管理',u'信息安全',u'虚拟化',u'虚拟现实',u'移动开发',u'硬件',u'游戏开发',u'语音识别',u'云计算',u'增强现实',u'桌面开发',u'自然语言处理']

    def __init__(self):
        self.document = {}
        self.wordDict = []

    def loadDoc(self): ##加载文档,格式如document.txt
        userlist = []
        for filename in os.listdir('/home/qistar/PycharmProjects/untitled1/KF/Browse'):
            user_id = filename.strip('Browse.txt')
            userlist.append(user_id)

        document = {}
        wordDict = []
        for f in userlist:
            print f
            f = codecs.open('/home/qistar/PycharmProjects/untitled1/KF/result/' + f + '.txt', 'rb', 'utf-8')
            data = f.readlines()
            for sentence in data:
                group = sentence.split(u':')
                document[group[0]] = group[1].strip('\n')
                wordslist = group[0].split(u',')
                for word in wordslist:
                    wordDict.append(word)
        self.document = document
        self.wordDict = set(wordDict)


    def fea_selection(self,wordlist): ##特征选择,先在加载数据,然后用chi选取特征词
        newwordlist = []
        self.loadDoc()
        chi = Chiextration(self.document)
        f1 = file('/home/qistar/PycharmProjects/untitled1/Model/Model6/chi.pk1','wb')
        pickle.dump(chi,f1,0)
        f1.close()

        for word in wordlist:
            for category in Feature_selection.categories:
                result = chi.ImproCalculateCHI(word, category)
                if result > 0.0001:
                    print word, category, result
                    newwordlist.append(word)
            print '---------------'

        return newwordlist

if __name__ == '__main__':
    str = u'服务器,数据,大数,大数据,数据库,客户端,用户，问题'
    wordlist = str.split(',')
    fea_extraction = Feature_selection()
    # joblib.dump(fea_extraction, '/home/qistar/PycharmProjects/untitled1/Model/Model6/model.m')
newwordlist = fea_extraction.fea_selection(wordlist)

# coding=utf-8
import chardet
import urllib2

url = "http://www.baidu.com"
data = (urllib2.urlopen(url)).read()
charset = chardet.detect(data)
code = charset['encoding']
content = str(data).decode(code, 'ignore').encode('utf8')
print content
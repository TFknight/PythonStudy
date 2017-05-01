# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

#page = 1
url = 'http://movie.mtime.com/219784/reviews/short/new.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8').replace("\n","")

    pattern = re.compile('<a target="_blank" title=".*?" href="(.*?)"><img width="48" height="48" src=".*?" alt=".*?"></a>')
    items = re.findall(pattern,content)
    for item in items:
       print item
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason


#
# string = "aaaaabbaaaabbb"
#  #print string
#  #string = string.replace("\n","")
#  #print string
# pattern = re.compile("(.+)")
# result = pattern.findall(string)
# print result


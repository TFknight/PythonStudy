# -*-coding:utf-8 -*-
import requests
import re
import time
url1 = "https://rate.tmall.com/list_detail_rate.htm?itemId=41881170071&spuId=289473817&sellerId=1031399035&order=3&currentPage="
url2 = "&append=0&content=1&tagId=&posi=&picture=&ua=106UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt%2BSnBMc096RHpHciQ%3D%7CU2xMHDJ7G2AHYg8hAS8XKAYmCE4vSTVEajxq%7CVGhXd1llXGldZ1tkWG1TbVBlUm9NeEB0Sn5Ef0B7Q39HeUxxS2Uz%7CVWldfS0RMQ01DjAQLg4gByBcciRy%7CVmhIGCcePgU9HSEdKRQ0ATsOOhomGCMYOAI5DCwQLhMvDzUMNWM1%7CV25OHjAePgozCCgUKhQhAT4APgpcCg%3D%3D%7CWGFBET8RMQQ7ASEeJRsvDzYPNg1bDQ%3D%3D%7CWWFBET8RMWFbYFt7RH9HelpgWGZEfEh2THRUa19qSnRPb1FlMxMuDiAOLhYqHyB2IA%3D%3D%7CWmNeY0N%2BXmFBfUR4WGZeZER9XWFcfEhoVG44&isg=AoaGbdEjIlr4tPaJLxPzGEL913XH28qhxAlTnHCuLqmScySN2HcasWwZPRFC&needFold=0&_ksTS=1489712188611_1727&callback=jsonp1728"
req = requests.session()
for i in range(1,1501):
    print "第" + str(i)  + "页评论"
    f = open('data2.txt','a')
    url_pinglun = url1 + str(i) + url2
    content = req.get(url_pinglun).text
    pinglun = re.findall("\"rateContent\":\"(.*?)\"",content)
    pinglun = set(pinglun)
    print "开始写入文件:"
    for j in pinglun:
        h = j.encode('utf-8')
        print h
        f.write(h)
        f.write('\n')
    f.close()
    time.sleep(3)



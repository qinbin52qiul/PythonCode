# -*- coding: utf-8 -*-
import urllib.request
import socket
import time
import re
import random

'''
利用 Python 爬虫刷 CSDN 文章的访问量
'''
# 博客地址
blog_url = [
    'https://blog.csdn.net/qq_34081993/article/details/80461123',
    'https://blog.csdn.net/qq_34081993/article/details/80330666',
    'https://blog.csdn.net/qq_34081993/article/details/80330719',
    'https://blog.csdn.net/qq_34081993/article/details/80330793',
    'https://blog.csdn.net/qq_34081993/article/details/79667287',
]
refererData = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=csdn%20%E6%80%9D%E6%83%B3%E7%9A%84%E9%AB%98%E5%BA%A6%20csdnzouqi&oq=csdn%20%E6%80%9D%E6%83%B3%E7%9A%84%E9%AB%98%E5%BA%A6&rsv_pq=fe7241c2000121eb&rsv_t=0dfaTIzsy%2BB%2Bh4tkKd6GtRbwj3Cp5KVva8QYLdRbzIz1CCeC1tOLcNDWcO8&rqlang=cn&rsv_enter=1&rsv_sug3=11&rsv_sug2=0&inputT=3473&rsv_sug4=3753'  # 伪装成是从baidu.com搜索到的文章
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 伪装成Chrome浏览器


class CSDN(object):
    def __init__(self, blog_url=blog_url, csdn_url="http://blog.csdn.net/qq_34081993"):
        self.blog_url = blog_url
        self.csdn_url = csdn_url
        self.headers = {'User-Agent': user_agent, 'Referer': refererData}

    def openBlog(
            self,
            link='http://blog.csdn.net/qq_34081993/article/details/79225558',
            timeout=60,
            sleepTime=22,
            maxTryNum=1):
        tries = 0
        maxNum = 0
        # for tries in range(maxTryNum):
        while tries < maxTryNum:
            try:
                socket.setdefaulttimeout
                # req = urllib.request.Request(link, None, self.headers)
                # resp = urllib.request.urlopen(req, None, timeout)
                # html = resp.read()
                print("Success!\t", )
                print("Rest ", sleepTime, " seconds to continue...\n")
                tries += 1
                time.sleep(sleepTime)
            # 在CSDN 判定为攻击时可以抛出异常, 继续下一次访问
            except Exception:
                if tries < (maxTryNum):
                    maxNum += 1
                    continue
                else:
                    print("Has tried %d times to access blog link %s, all failed!" % (maxNum, link))
                    break

    def start(self,
              maxTime=100,  # maxTime 为访问 blog_url 列表的迭代次数
              sleepTimeStart=5,  # sleepTimeMin 为最小睡眠时间
              sleepTimeEnd=15,  # sleepTimeMax 为最大睡眠时间
              timeout=60):  # timeout 为 blog_url 访问的最大等待时间
        # 访问列表是随机访问的,maxTime 为访问列表的迭代次数,每次迭代的具体数量 为 len(self.blog_url)
        # 因为是随机访问，所以访问一轮下来并非是每一篇博客都会访问到
        for i in range(maxTime * len(self.blog_url)):
            # 随机访问 blog_url 列表
            randomLink = random.choice(self.blog_url)
            print('This tinme the random_blog link is ', randomLink)
            self.openBlog(
                link=randomLink,
                sleepTime=random.uniform(sleepTimeStart, sleepTimeEnd),  # 一篇博客的具体时间由随机数控制
                timeout=timeout)
            print("Now is " + str(i + 1) + " times to acess blog link\n")


csdn = CSDN()
inputMaxTime = input(u'请输入列表访问次数\n')
csdn.start(maxTime=int(inputMaxTime))

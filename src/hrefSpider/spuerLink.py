'''
Created on 2016年12月3日

@author: fandong
'''
from urllib.request import urlopen
from bs4 import  BeautifulSoup
import re
import datetime
import random
from urllib.parse import urlparse
from urllib.error import HTTPError

pages=set()
random.seed(datetime.datetime.now())
#获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
    includeUrl=urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    print(includeUrl+"'fasdf")
    internalLinks=[]
    #找到所有以‘／’开头的连接
    try:
        for link in bsObj.findAll("a",href=re.compile("^("+includeUrl+"|/)[/].*$")):
            if link.attrs["href"] is not None:
                if link.attrs["href"] not in internalLinks:
                    if(link.attrs["href"].startswith("/")):
                        internalLinks.append(includeUrl+link.attrs["href"])
                    else:
                        internalLinks.append(link.attrs["href"])
        if len(internalLinks)==0:
            print("internalLinks 长度为0")
        return internalLinks
    except AttributeError as e:
        print("Attrs 错误信息")
    #except Exception as e:
     #   print("getInternalLinks 异常")

#获取页面的所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    #找出所有以“http”或“www”开头且不包括当前URL的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks
    

def getRandomExternalLink(startingPage):
    try:
        html=urlopen(startingPage)
        bsObj=BeautifulSoup(html)
        for namelist in getExternalLinks(bsObj,urlparse(startingPage).netloc):
            print(namelist)
        externalLinks=getExternalLinks(bsObj,urlparse(startingPage).netloc)
        if len(externalLinks)==0:
            print("没有外部链接，查看网站")
            print(urlparse(startingPage).scheme)
            domain=urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
            print(domain)
            internalLinks=getInternalLinks(bsObj, domain) 
            if len(internalLinks)>0:    
                return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
            else:
                return internalLinks.append("http://www.baidu.com")
        else:
            return externalLinks[random.randint(0,len(externalLinks)-1)]
    except HTTPError as e:
        print("http 异常")
    
    
#开始调用方法
def followExternalOnly(startingSite):
    try:
        externalLink=getRandomExternalLink(startingSite)
        print("Random external link is :"+externalLink)
        followExternalOnly(externalLink)
    except SystemError as e:
        print(" 123")
    

followExternalOnly("http://www.cnblogs.com")
#调用内部链接查询
#html=urlopen("http://www.cnblogs.com")
#bsObj=BeautifulSoup(html)
#for name in getInternalLinks(bsObj,"http://www.cnblogs.com"):
#    print(name)
#for link in bsObj.findAll("a",href=re.compile("^http://www.cnblogs.com/.*$")):
 #   print(link.attrs["href"])
        
#for name in getExternalLinks(bsObj,urlparse("http://www.cnblogs.com").netloc):
#    print(name)
    
        
                              


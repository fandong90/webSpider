'''
Created on 2016年12月3日

@author: fandong
'''
from urllib.request import urlopen
from urllib.parse import urlparse
def printHello():
    print('hello!')
    
printHello()
html=urlopen("http://www.cnblogs.com")
print(html.read())
print(urlparse("http://www.cnblogs.com").netloc)
print(urlparse(urlparse("http://www.cnblogs.com").netloc).netloc+";;;")

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 00:30:18 2020

@author: asif
"""


import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("enter the xml link: ")

print('Retrieving',url)
uh=urllib.request.urlopen(url,context=ctx)
data=uh.read()
print('Retrieved',len(data),'characters')
data=data.decode()
Tree=ET.fromstring(data)
lst=[]
cmmnt=Tree.findall('comments/comment')
for count in cmmnt:
    lst.append(int(count.find('count').text))
print('Count: ',len(lst))
print('Sum: ',sum(lst))
    
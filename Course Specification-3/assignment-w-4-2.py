# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 03:10:32 2020

@author: asif
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("enter link= ")
html=urlopen(url,context=ctx).read()
sop=BeautifulSoup(html,"html.parser")

count=int(input("Enter count: "))
pos=int(input("Enter position: "))

for n in range(count):
    tags=sop('a')
    i=1
    for tag in tags:
        if i==pos:
            if n==count-1:
                print(tag.contents[0])
                break
            url=tag.get('href',None)
            print("Retrieving: ",url)
            html=urlopen(url,context=ctx).read()
            sop=BeautifulSoup(html,"html.parser")
            break
        i+=1
        
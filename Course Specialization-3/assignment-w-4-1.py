# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("enter link= ")
html=urlopen(url,context=ctx).read()
soupp=BeautifulSoup(html,"html.parser")

tags=soupp('span')
lst=list()
count=0

for tag in tags:
    st=tag.contents[0]
    st=st.strip()
    lst.append(int(st))
    count+=1
print(count)
print(sum(lst))

    


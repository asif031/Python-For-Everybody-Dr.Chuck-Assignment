# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:03:00 2020

@author: asif
"""
import re
fh=open("regex_sum_781000.txt",encoding="utf-8")
lst=list()
ret=list()
for lines in fh:
    lines=lines.strip()
    ret=re.findall("[0-9]+",lines)
    for num in ret:
        if num!='':
            lst.append(int(num))
print(sum(lst))

    
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 01:31:30 2020

@author: asif
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for lines in handle:
    if not lines.startswith("From "):
        continue
    words=lines.split()
    counts[words[1]]=counts.get(words[1],0)+1
most_key=None
most_value=None
for key,value in counts.items():
    if most_value==None or value>most_value:
        most_value=value
        most_key=key
print(most_key,most_value)
   


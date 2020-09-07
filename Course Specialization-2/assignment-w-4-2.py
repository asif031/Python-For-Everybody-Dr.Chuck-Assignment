# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 01:30:06 2020

@author: asif
"""


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "): continue
    line=line.rstrip()
    words=line.split()
    print(words[1])
    count+=1

print("There were", count, "lines in the file with From as the first word")

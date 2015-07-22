__author__ = 'le-user'
import sys
# -*- coding: utf-8 -*-
input=sys.stdin.readline()
n=int(input)
flg=True
if n<2:
    flg=False
elif n>2:
    list=range(2,n)
    for i in list:
        if n%i==0:
            flg=False
print(flg)







__author__ = 'le-user'
import sys
# -*- coding: utf-8 -*-

def prime(n):
    flg=True
    if n<2:
        flg=False
    elif n>2:
        list=range(2,n)
        for i in list:
            if n%i==0:
                flg=False
    return flg

input=sys.stdin.readline()
n=int(input)
for i in range(1,n+1):
   print(i,end=" ")
   print(prime(i))






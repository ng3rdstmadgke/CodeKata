__author__ = 'midorikawa.keita'
# -*- coding: utf-8 -*-
import sys

n=sys.stdin.readline()
c=int(n)
t=1
for i in range(10):
    t=(t+c/t)/2.0
print(t)
__author__ = 'midorikawa.keita'
import sys
# -*- coding: utf-8 -*-
input=sys.stdin.readline()
year=int(input)

def leap_year(n):
    flg=False
    if n%4==0:
        flg=True
    if n%100==0:
        flg=False
    if n%400==0:
        flg=True
    return flg

print(leap_year(year))

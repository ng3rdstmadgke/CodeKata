__author__ = 'midorikawa.keita'
import sys
# -*- coding: utf-8 -*-
def func(str):
    list=str.split(" ")
    num=""
    for i in range(len(list)):
        if i==0:
            digits=list[0]
        else:
            digits="0"
        num+=digits
    return num

if __name__=="__main__":
    input=input("スペース区切りで値を入力して下さい：")
    print(func(input))

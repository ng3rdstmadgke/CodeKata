__author__ = 'midorikawa.keita'
import sys
# -*- coding: utf-8 -*-
def func(str):
    list=str.split(" ")
    for i in range(len(list)):
        if i==0:
            print(list[0],end=" ")
        else:
            print("0",end=" ")

input=input("スペース区切りで値を入力して下さい：")
func(input)

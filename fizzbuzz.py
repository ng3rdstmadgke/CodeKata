__author__ = 'le-user'
# -*- coding: utf-8 -*-
def fizzbuzz(number):
    for num in range(1,number+1):
        if num%3==0:
            print("Fizz",end="")
        if num%5==0:
            print("Buzz",end="")
        if num%3!=0 and num%5!=0:
            print(num,end="")
        print(" ",end="")

input=input("数字を入力してください")
n=int(input)
print(fizzbuzz(n))
__author__ = 'le-user'
# -*- coding: utf-8 -*-
for num in range(1,101):
    if num%3==0:
        print("Fizz")
    if num%5==0:
        print("Buzz")
    if num%3!=0 and num%5!=0:
        print(num)

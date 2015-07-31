__author__ = 'le-user'
# -*- coding: utf-8 -*-
def fizzbuzz(num):
    i=""
    if num%3==0:
        i+="Fizz"
    if num%5==0:
        i+="Buzz"
    if num%3!=0 and num%5!=0:
        i+=str(num)
    return i

if __name__ == "__main__":
    n=int(input("数字を入力してください"))

    for i in range(1,n+1):
        print(fizzbuzz(i),end=" ")
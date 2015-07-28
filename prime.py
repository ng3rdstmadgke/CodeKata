__author__ = 'le-user'
import sys
# -*- coding: utf-8 -*-

def my_prime(n):
    flg=True
    if n<2:
        flg=False
    elif n>2:
        list=range(2,n)
        for i in list:
            if n%i==0:
                flg=False
    return flg

if __name__ == "__main__":
    n=int(sys.stdin.readline())

    if my_prime==True:
        print("{}は素数です。".format(prime(n)))
    else:
        print("{}は素数ではありません。".format(prime(n)))

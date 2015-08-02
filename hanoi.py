__author__ = 'midorikawa.keita'
# -*- coding: utf-8 -*-

def my_hanoi(n,a,c,b):
    if n>0:
        my_hanoi(n-1,a,b,c)
        print("{0}を{1}から{2}に移動".format(n,a,c))
        my_hanoi(n-1,b,c,a)

if __name__=="__main__":
    my_hanoi(3,"A","C","B")



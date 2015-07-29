__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
"""
フィボナッチ数列とは下記の数列のように今の項と前項の和が次の項となるような数列です。

1 1 2 3 5 8 13 21 34 55 89 144

課題1 フィボナッチ数列の第n項を求めるプログラムを再帰呼出しを用いて書いて下さい。ただしnはコマンドライン引数で得るものとします。
課題2 フィボナッチ数列の第n項を求めるプログラムを再帰呼出しを用いずに書いて下さい。ただしnはコマンドライン引数で得るものとします。
課題3 再帰呼出しを用いた場合と用いない場合、どちらがどのような点で優れているかを考えて下さい
"""
#再起処理を用いる関数
def make_fibonacci_1(n,i,j):
    if n-3>0:
        ret = make_fibonacci_1(n-1,j,i+j)
        return ret
    return i+j

#再起処理を用いない関数
def make_fibonacci_2(n):
    list=[1,1]
    for i in range(n-2):
        num=list[i]+list[i+1]
        list.append(num)
    return list[n-1]

if __name__=="__main__":
    a=make_fibonacci_1(5,1,1)
    print(a)
    b=make_fibonacci_2(5)
    print(b)

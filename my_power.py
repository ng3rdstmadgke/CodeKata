__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
"""
aのn乗を返すような2引数の関数（メソッド）を下記の方法で作って下さい。
ただしa, nは正整数とします。（0や負の数に関しては考慮しなくても結構です。）
課題1. aをn回かけるループ文を使って作って下さい。

課題2. 課題1で作った物より高速なものを作って下さい。（計算時間のオーダーがlg(n)となるように）。
計算時間のオーダーがlg(n)というのは平たく言えばnに対して計算の手間（例えばループ回数）がおおよそlg(n)回ということです。
ここではnが8程度ならば凡そ3回、1024程度ならば凡そ10回の手間で計算できる、というように解釈していただければ構いません。
"""
def my_power_1(a,n):
    j=1
    for i in range(n):
        j*=a
    return j

def my_power_2(p,n):
    w=1
    bin_num=bin(n)[2:]
    for i in range(len(bin_num)):
        if bin_num[i]==1:
            w=w**2*p
        else:
            w=w**2
    return w

__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
import random
def max_sub_num():
    #1~1000までのリストを作成(int)
    st_list=list(range(1,1001))
    num_list=[]
    #数字をランダムに８つ選び、リストにする。
    for i in range(8):
        n=random.choice(st_list)
        num_list.append(n)
        st_list.remove(n)
    print(num_list)
    #一番大きい数字を探し、その数字と添字を表示し、num_listの数字をに置換する

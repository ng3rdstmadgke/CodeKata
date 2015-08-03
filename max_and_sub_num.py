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
    #一番大きい数字を探し、その数字と添字を表示し、num_listのその数字を0に置換する
    answer=[]
    for i in range(3):
        max_num=max(num_list)
        sub_num=num_list.index(max_num)
        print(str(sub_num)+"->"+str(max_num))
        num_list[sub_num]=0
    return answer

if __name__=="__main__":
    max_sub_num()
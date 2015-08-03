__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
import sys
def my_eto(year):
    #干支のリストを作る
    eto=list("子丑寅卯辰巳午未申酉戌亥")
    #西暦-4を１２で割ってあまりで干支リストをインデックスする
    t=(int(year)-4)%12
    return eto[t]

if __name__=="__main__":
    year=sys.stdin.readline()
    print(my_eto(year))

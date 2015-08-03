__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
import sys
def my_eto(year):
    #干支のリストを作る
    eto=list("子丑寅卯辰巳午未申酉戌亥")
    #西暦-4を１２で割ってあまりで干支リストをインデックスする
    t=(year-4)%12
    return eto[t]

if __name__=="__main__":
    year=int(sys.stdin.readline().rstrip())
    print("{}年は{}年です".format(year,my_eto(year)))

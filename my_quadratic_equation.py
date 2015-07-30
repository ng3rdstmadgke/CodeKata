__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
from _decimal import Decimal
import math
"""
ax^2+bx+c=0 の解を求める3引数の関数（メソッド）を作って下さい。
ただし、aは0ではなく、虚数解は考えなくても結構です。
課題2. 上記で作ったプログラムにa=0.0000000045, b=10, c=1などの値を代入し、
得られた結果と 実際の解とを比較し大きな誤差があった場合プログラムの問題点を考察して下さい。
可能ならばより正確な答えがでる関数を作って下さい。
"""
def quadratic_equation(a,b,c):
    aa=Decimal(a)
    bb=Decimal(b)
    cc=Decimal(c)
    i=Decimal(2)
    j=Decimal(4)
    n=Decimal(0.5)

    ans_1=(-bb+(bb**i-j*aa*cc)**n)/(i*aa)
    ans_2=(-bb-(bb**i-j*aa*cc)**n)/(i*aa)
    return [ans_1,ans_2]









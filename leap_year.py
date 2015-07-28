__author__ = 'midorikawa.keita'
import sys
# -*- coding: utf-8 -*-


def leap_year(n):
    flg=False
    if n%4==0:
        flg=True
    if n%100==0:
        flg=False
    if n%400==0:
        flg=True
    return flg

if __name__ == "__main__":
    input_year=int(sys.stdin.readline())
    if leap_year(input_year)==True:
        print("うるう年です。")
    else:
        print("うるう年ではありません。")

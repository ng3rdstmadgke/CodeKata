__author__ = 'midorikawa.keita'
import random
# -*- coding: utf-8 -*-

#ランダムで数字を生成1~100まで
right_num=random.randint(1,100)
#正解が出るまでループ処理
while True:
    #プレイヤーの数値入力
    input_num=input("数字を入力してください：")
    player_num=int(input_num)
    #if　入力された数字が正解の場合
    if player_num==right_num:
        break
    #elif　入力された数字が正解より大きい場合
    elif player_num>right_num:
        print(str(player_num)+"は正解よりも大きい数字です")
    #elif　入力された数字が正解より小さい場合
    elif player_num<right_num:
        print(str(player_num)+"は正解よりも小さい数字です")

#出力→（正解です）
print("正解です!!")
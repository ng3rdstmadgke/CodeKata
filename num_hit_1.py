__author__ = 'midorikawa.keita'
import random
# -*- coding: utf-8 -*-
def num_judge(player_num,correct_num):
    #if　入力された数字が正解の場合
    if player_num==correct_num:
        flg=0
    #elif　入力された数字が正解より大きい場合
    elif player_num>correct_num:
        flg=1
    #elif　入力された数字が正解より小さい場合
    elif player_num<correct_num:
        flg=2
    return flg

if __name__=="__main__":
    #ランダムで数字を生成1~100まで
    correct_num=random.randint(1,100)
    #正解が出るまでループ処理
    while True:
        #プレイヤーの数値入力
        player_num=int(input("数字を入力してください："))


        #数値があっているかの判断
        flg=num_judge(player_num,correct_num)


        #if　入力された数字が正解の場合
        if flg==0:
            break
        #elif　入力された数字が正解より大きい場合
        elif flg==1:
            print(str(player_num)+"は正解よりも大きい数字です")
        #elif　入力された数字が正解より小さい場合
        elif flg==2:
            print(str(player_num)+"は正解よりも小さい数字です")

    #出力→（正解です）
    print("正解です!!")
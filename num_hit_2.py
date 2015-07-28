__author__ = 'midorikawa.keita'
import random
# -*- coding: utf-8 -*-
#正解数の生成
def num_gen(digits):
    number_list=["1","2","3","4","5","6","7","8","9"]
    correct_num=""
    for i in range(digits):
        choice_num=random.choice(number_list)
        correct_num+=choice_num
        number_list.remove(choice_num)
    return correct_num

#桁の判定用関数
def digit_judge(correct_num,player_num):
    h=0
    #for　桁数n回のループ（桁の判定）
    for i in range(digits):
        #if　正解値[n]==入力値[n]
        if correct_num[i]==player_num[i]:
            #h+=1
            h+=1
    return h

#数値の判定用関数
def num_judge(correct_num,player_num):
    b=0
    #for　桁数n回のループ（数値一致の判定）
    for i in range(digits):
        #if　入力値[n]　in　正解値
        if player_num[i] in correct_num:
            #b+=1
            b+=1
    return b


if __name__=="__main__":
    digits=random.randint(1,9)
    print("桁数は"+str(digits)+"です。")

    #ランダムでnケタの数字を発生→すべての位は1~9の異なる数字で構成される(文字列型として処理)関数
    correct_num=num_gen(digits)
    #正解までのループ
    while True:
        #プレイヤーの入力
        player_num=input(str(digits)+"桁の数値を入力してください")
        if len(player_num)!=len(correct_num):
            continue

        #if　正解値==入力値
        if correct_num==player_num:
            #break
            break

        #桁の判定用関数
        h=digit_judge(correct_num,player_num)

        #数値の判定用関数
        b=num_judge(correct_num,player_num)

        #print　h hit b blow
        print(str(h)+"hit "+str(b)+"blow")

    #print 正解！
    print("正解!!")



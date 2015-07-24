__author__ = 'midorikawa.keita'
import random
# -*- coding: utf-8 -*-
#何桁の数字にするかを1～9桁の間からランダムで選ぶ
digits=random.randint(1,9)
#何桁の数字を表示
print("桁数は"+str(digits)+"です。")

#ランダムでnケタの数字を発生→すべての位は1~9の異なる数字で構成される(文字列型として処理)
number_list=["1","2","3","4","5","6","7","8","9"]
right_num=""
for i in range(digits):
    choice_num=random.choice(number_list)
    right_num+=choice_num
    number_list.remove(choice_num)
#print(right_num)

#正解までのループ
while True:
    #プレイヤーの入力
    player_num=input(str(digits)+"桁の数値を入力してください")
    if len(player_num)!=len(right_num):
        continue

    #if　正解値==入力値
    if right_num==player_num:
        #break
        break

    #桁の判定用変数h=0
    h=0
    #for　桁数n回のループ（桁の判定）
    for i in range(digits):
        #if　正解値[n]==入力値[n]
        if right_num[i]==player_num[i]:
            #h+=1
            h+=1

    #数値の判定用変数b=0
    b=0
    #for　桁数n回のループ（数値一致の判定）
    for i in range(digits):
        #if　入力値[n]　in　正解値
        if player_num[i] in right_num:
            #b+=1
            b+=1

    #print　h hit b blow
    print(str(h)+"hit "+str(b)+"blow")

#print 正解！
print("正解!!")



__author__ = 'midorikawa.keita'
# -*- coding: utf-8 -*-
import random

#テキストファイルの読み込み
    #テキストファイルをリスト化
text_list=["abc","cde","efg","ghi","ijk","klm","mno","opq","qrs","stu","uvw","wxy","yza"]
#残りの単語のリストを作成
used_list=["abc","cde","efg","ghi","ijk","klm","mno","opq","qrs","stu","uvw","wxy","yza"]
#使用済み単語のリストを作成
used_word_list=[]
#CPUとuserの使用した単語のリストを作成
user_list=[]
cpu_list=[]
#乱数により先行と後攻を決定（0ならcpu,1なら自分）
turn=random.choice([0,1])
#if　0なら
if turn==0:
    #ランダムでリストの中から単語を出力→単語を表示→リストから単語を削除→cpuリスト＆使用済み単語リストに単語を追加
    cpu_word=random.choice(used_list)
    print(cpu_word)
    used_list.remove(cpu_word)
    used_word_list.append(cpu_word)
    cpu_list.append(cpu_word)
#フラグ（0,1,2）
win_lose=0

#while True
while True:
    #自分：リストの中から単語を選択→
    user_word=input("あなたのターンです：")

    #辞書にない単語を入力すると再入力を促す→ループさせる
    while text_list.count(user_word)==0:
        user_word=input("リストにある単語を入力してください:")



    if len(cpu_list)!=0:
        #if　すでに使った単語を使用していないか→TorF
        if used_word_list.count(user_word)!=0:
            #フラグ1
            win_lose=1
            break
            #if　前の単語の末尾の文字が自分の単語の先頭に来ているか→TorF→先攻がCPUのときのみ作動するようにする。
        if user_word[0]!=cpu_word[-1]:
            #フラグ2
            win_lose=2
            break

     #リストから単語を削除
    used_list.remove(user_word)
     #使用した単語をリストに要素を追加
    used_word_list.append(user_word)
    #使用した単語をuserリストに追加
    user_list.append(user_word)

    #if　リストの中に単語が残っているか→TorF
    if len(used_list)==0:
        #フラグ0
        win_lose=0
        break

#cpu：リストの中から前の単語の末尾の文字が単語の先頭に来ている単語を選択
    for i in used_list:
        if user_word[-1]==i[0]:
            cpu_word=i

    print(cpu_word)
    #リストから単語を削除
    used_list.remove(cpu_word)
    #使用した単語をリストに要素を追加
    used_word_list.append(cpu_word)
    #使用した単語をcpuリストに追加
    cpu_list.append(cpu_word)

    #if　リストの中に単語が残っているか→TorF
    if len(used_list)==0:
        #フラグ0
        win_lose=0
        break


#if　フラグ1ならば
if win_lose==1:
    #すでに使った単語がリストの何番目にあるか
    double=used_word_list.index(user_word)
    #どっちがダブった単語を使っているか
    if cpu_list.count(user_word)==1:
        i="わたし"
    elif user_list.count(user_word)==1:
        i="あなた"


#if
if win_lose==0:
    #フラグ0→「まいりました！あなたの勝ちです。　今回のしりとりでは [使用単語数] 個の単語を使用しました。」
    print("まいりました！あなたの勝ちです。今回のしりとりでは"+str(len(used_word_list))+"個の単語を使用しました")
elif win_lose==1:
    #フラグ1→「その言葉は [回数] 回目に [あなた|わたし] が使用しています。わたしの勝ちです。今回のしりとりでは [使用単語数] 個の単語を使用しました。」
     print("その言葉は"+str(double+1)+"回目に"+str(i)+"が使用しています。わたしの勝ちです。今回のしりとりでは"+str(len(used_word_list))+"個の単語を使用しました")
else:
    #フラグ2→「その言葉は間違っています。わたしの勝ちです。今回のしりとりでは [使用単語数] 個の単語を使用しました。」
    print("その言葉は間違っています。わたしの勝ちです。今回のしりとりでは"+str(len(used_word_list))+"個の単語を使用しました")
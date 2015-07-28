__author__ = 'midorikawa.keita'
# -*- coding: utf-8 -*-
import random


#プレイヤーの単語をジャッジ
def player_judge(word_now,word_before,used_list):
    flg=0
    #if　すでに使った単語を使用していないか
    if used_list.count(word_now)!=0:
        #フラグ1
        flg=1
    #if　前の単語の末尾の文字が自分の単語の先頭に来ているか
    if word_now[0]!=word_before[-1]:
        #フラグ2
        flg=2
    return flg

#単語の削除と追加
def dict_update(word,cpu_dict,used_list):
    if word in cpu_dict:
        cpu_dict.remove(word)
    used_list.append(word)

#cpu_dictの中に単語が残っているか
def word_left(cpu_dict):
    flg=0
    if len(cpu_dict)==0:
        flg=3


#cpuの単語選び
def cpu_act(word_before,cpu_dict):
    list=[]
    for i in cpu_dict:
        if word_before[-1]==i[0]:
            list.append(i)
    if len(list)==0:
        cpu_word=0
    else:
        cpu_word=random.choice(list)

    return cpu_word

#重複単語を最初に使った人
def double_word(used_list,player_word):
    if turn==0:
        if (used_list.index(player_word)+1)%2==0:
            i="わたし"
        else:
            i="あなた"
    if turn==1:
        if (used_list.index(player_word)+1)%2==0:
            i="あなた"
        else:
            i="わたし"

        return i

#結果の出力
def game_result(win_lose,player_word,used_list):
    if win_lose==1:
        double=used_list.index(player_word)
        i=double_word(used_list,player_word)
        #フラグ1→「その言葉は [回数] 回目に [あなた|わたし] が使用しています。わたしの勝ちです。今回のしりとりでは [使用単語数] 個の単語を使用しました。」
        print("その言葉は"+str(double+1)+"回目に"+str(i)+"が使用しています。わたしの勝ちです。今回のしりとりでは"+str(len(used_list))+"個の単語を使用しました")
    elif win_lose==2:
        #フラグ2→「その言葉は間違っています。わたしの勝ちです。今回のしりとりでは [使用単語数] 個の単語を使用しました。」
        print("その言葉は間違っています。わたしの勝ちです。今回のしりとりでは"+str(len(used_list))+"個の単語を使用しました")
    elif win_lose==3:
        #フラグ0→「まいりました！あなたの勝ちです。　今回のしりとりでは [使用単語数] 個の単語を使用しました。」
        print("まいりました！あなたの勝ちです。今回のしりとりでは"+str(len(used_list))+"個の単語を使用しました")





if __name__ == "__main__":
    #cpuが使用する辞書を作成
    cpu_dict=["abc","ac","cde","efg","ghi","ijk","klm","mno","opq","qrs","stu","uvw","wxy","yza"]
    #使用済み単語のリストを作成
    used_list=[]
    #先攻・後攻の決定
    turn=random.choice([0,1])
    #勝ち負けフラグの初期値
    win_lise=0
    #if turn==0
    if turn==0:
        #cpuが単語をランダム選択
        cpu_word=random.choice(cpu_dict)
        dict_update(cpu_word,cpu_dict,used_list)
        print(cpu_word)
        #しりとりループ

        while True:
            #自分→単語を入力（1.すでに使っている単語を使用していないか。2.前単語の末尾が単語の先頭に来ているか。）
            player_word=input("あなたのターンです：")
            #入力単語が正しいかを判別しフラグを立てる(0~)
            win_lose=player_judge(player_word,cpu_word,used_list)
            #入力した単語を使用済み単語リストに追加
            dict_update(player_word,cpu_dict,used_list)
            #cpu_dictの中に単語が残っているか
            word_left(cpu_dict)
            #フラグが0以外だったらbreak
            if win_lose!=0:
                break

            #CPU単語選び
            cpu_word=cpu_act(player_word,cpu_dict)
            #入力した単語を使用済み単語リストに追加
            dict_update(cpu_word,cpu_dict,used_list)
            #cpuが使う言葉がなかったらbreak
            if cpu_word==0:
                win_lose=3
                break
            print(cpu_word)

    #else:
    elif turn==1:
        #自分で単語を入力
        player_word=input("あなたのターンです：")
        #しりとりループ
        while True:
            #CPU単語選び
            cpu_word=cpu_act(player_word,cpu_dict)
            #入力した単語を使用済み単語リストに追加
            dict_update(cpu_word,cpu_dict,used_list)
            #帰ってきたワードが0だったらbreak
            if cpu_word==0:
                win_lose=3
                break
            print(cpu_word)

            #自分→単語を入力（1.すでに使っている単語を使用していないか。2.前単語の末尾が単語の先頭に来ているか。）
            player_word=input("あなたのターンです：")
            #入力単語が正しいかを判別しフラグを立てる(0~)
            win_lose=player_judge(player_word,cpu_word,used_list)
            #入力した単語を使用済み単語リストに追加
            dict_update(player_word,cpu_dict,used_list)
            #cpu_dictの中に単語が残っているか
            word_left(cpu_dict)
            #cpuが使う言葉がなかったらbreak
            if win_lose!=0:
                break
    #出力
    game_result(win_lose,player_word,used_list)


__author__ = 'midorikawa.keita'
# -*- coding: utf-8 -*-
#暗号鍵を基にしたディクショナリーを作成
def code_dict(key_num):
    dict={}
    code_base=list("abcdefghijklmnopqrstuvwxyz .,-")
    code_key=code_base[key_num:]+code_base[0:key_num]
    #print(code_base)
    #print(code_key)
    for i in range(30):
        dict[code_base[i]]=code_key[i]
    #print(dict.items())
    return dict

#ディクショナリーに代入して暗号を解読
def decode(dict,code):
    code_list=list(code)
    #print(code_list)
    str=""
    for i in code_list:
        if i!=";":
            str+=dict[i]
        else:
            str+=i
    return str


#暗号文を入力
code=input("暗号を入力してください：")

for i in range(1,31):
    #暗号鍵を基にしたディクショナリーを作成(関数で作成）
    key_dict=code_dict(i)
    #暗号文をディクショナリーに代入して解読(関数で作成）
    answer=decode(key_dict,code)
    #出力
    print(answer,end="\n\n")


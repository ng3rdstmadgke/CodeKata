__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
"""
str=bin(ord("0"))[2:]
if len(str)>8:
    t=str.rjust(16,"0")
else:
    t=str.rjust(8,"0")
print(t)
"""
def base64_dict():
    base_dict={}
    value_list=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    key_list=[]
    for i in range(64):
        num_bin=bin(i)[2:].rjust(6,"0")
        key_list.append(num_bin)
    for i in range(64):
        base_dict[key_list[i]]=value_list[i]
    return base_dict

def convert_text(text):
    bin_text=""
    for i in range(len(text)):
        str=bin(ord(text[i]))[2:]
        if len(str)>8:
            t=str.rjust(16,"0")
        else:
            t=str.rjust(8,"0")
        bin_text+=t
    if len(bin_text)%6!=0:
        for i in range(6-(len(bin_text)%6)):
            bin_text+="0"
    return bin_text

def code_base64(bin_text,base_dict):
    code=""
    for i in range(int(len(bin_text)/6)):
        key=bin_text[i*6:i*6+5]
        value=base_dict[key]
        code+=value
    if len(code)%4!=0:
        for i in range(4-(len(code)%4)):
            code+="="
    return code














#文章入力
#Base64の辞書を作成

#文章を2進数に変換
#2進数に変換した文字列を6文字区切りにして辞書にぶち込む
#出力
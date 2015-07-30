__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
import sys

#6桁の2進数と英数字を結びつける辞書を作る関数
def base64_dict():
    base_dict={}
    value_list=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    #print(len(value_list)) value_listの長さ=64　OK
    key_list=[]
    for i in range(64):
        num_bin=bin(i)[2:].rjust(6,"0")
        key_list.append(num_bin)
    #print(len(key_list)) key_listの長さ=64 OK
    for i in range(64):
        base_dict[key_list[i]]=value_list[i]
    return base_dict

#テキストを8桁と16桁の2進数に変換して、文字列としてreturnする関数
def convert_text(text):
    bin_text=""
    for i in range(len(text)):
        str=bin(ord(text[i]))[2:]
        if len(str)>8:
            t=str.rjust(16,"0")
        else:
            t=str.rjust(8,"0")
        #print(t,end=" ") tの桁数　8と16桁　OK
        bin_text+=t
    if len(bin_text)%6!=0:
        for i in range(6-(len(bin_text)%6)):
            bin_text+="0"
    #print(len(bin_text)%6) bin_textの長さ　6で割り切れる　OK
    return bin_text

#2進数に変換した文字列を6文字区切りにし、辞書を用いて英数字に変換する関数
def code_base64(bin_text,base_dict):
    code=""
    for i in range(int(len(bin_text)/6)):
        key=bin_text[i*6:i*6+6]
        value=base_dict[key]
        code+=value
    if len(code)%4!=0:
        for i in range(4-(len(code)%4)):
            code+="="
    return code

if __name__=="__main__":
    input_text=sys.stdin.readline()
    my_dict=base64_dict()
    bin_text=convert_text(input_text)
    return_code=code_base64(bin_text,my_dict)
    print(return_code)

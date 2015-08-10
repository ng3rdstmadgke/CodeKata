__author__ = 'midorikawakeita'

import sys
"""
入力例
# ########
# ## ### #
#    ##  #
####    ##
# ## #####
#    #   #
# #### # #
#      # #
## ## ## #
######## #
出力例
#+########
<<<<<<< HEAD
#+##0###0#
#++++##00#
####+000##
#0##+#####
#++++#+++#
#+####+#+#
#++++++#+#
##0##0##+#
########+#
"""
#def my_maze(maze_text):
    #迷路の入力を行列の形式に変換

    #迷路の入力→入力形式は行列（迷路は"#"と" "で構成）
    #" "の部分をすべて+に置換
    #３方向が"#"または" "に囲まれているマスを" "に置換
list_l=[]
while True:
    input=sys.stdin.readline().strip()
    if len(input)==0:
        break
    input_plus=input.replace(" ","+")
    list_s=[]
    for i in input_plus:
        list_s.append(i)
    list_l.append(list_s)
print(list_l)

while True:
    break_num=0
    for i in range(len(list_l)):
        j_num=0
        for n in range(len(list_l[i])):
            if i!=0 and i!=len(list_l)-1 and n!=0 and n!=len(list_l[0])-1 and list_l[i][n]=="+":
                if list_l[i-1][n]=="#":
                    j_num+=1
                if list_l[i][n-1]=="#":
                    j_num+=1
                if list_l[i][n+1]=="#":
                    j_num+=1
                if list_l[i+1][n]=="#":
                    j_num+=1
                if j_num>2:
                    list_l[i][n]=" "
    if break_num==0:
        break

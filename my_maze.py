<<<<<<< HEAD
__author__ = 'midorikawakeita'
=======
__author__ = 'midorikawa'
>>>>>>> origin/master
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
list=[]
while True:
    input=sys.stdin.readline().rstrip()
    if len(input)==0:
        break
    i=input.replace(" ","+")
    list.append(i)
print(list[0][2])
print(list)
while True:
    break_num=0
    for i in range(len(list)):
        j_num=0
        for n in range(len(list[i])):
            if i!=0 and i!=len(list)-1 and n!=0 and n!=len(list[0])-1 and list[i][n]=="+":
                if list[i-1][n]=="#":
                    j_num+=1
                if list[i][n-1]=="#":
                    j_num+=1
                if list[i][n+1]=="#":
                    j_num+=1
                if list[i+1][n]=="#":
                    j_num+=1
                if j_num>2:
                    break_num+=1
                    update_line=str(list[i])
    if break_num==0:
        break
print(list)
=======
#+## ### #
#++++##  #
####+   ##
# ##+#####
#++++#+++#
#+####+#+#
#++++++#+#
## ## ##+#
########+#
"""

def make_maze(maze_list):
    for i in range(len(maze_list)):
        for j in range(len(maze_list[i])):
            if



if __name__=="__main__":
    maze_list=[]
    while True:
        input=sys.stdin.readline().rstrip("\n")
        if input:
            input_line=input.replace(" ","+")
            input_list=list(input_line)
            maze_list.append(input_list)
        else:
            break


>>>>>>> origin/master

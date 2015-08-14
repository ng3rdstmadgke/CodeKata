__author__ = 'midorikawa'
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

    while True:
        break_num=0
        for i in range(len(maze_list)):
            for n in range(len(maze_list[i])):
                j_num=0
                if i>0 and i<len(maze_list)-1 and n>0 and n<len(maze_list[i])-1 and maze_list[i][n]=="+":
                    if maze_list[i][n-1]=="#" or maze_list[i][n-1]==" ":
                        j_num+=1
                    if maze_list[i-1][n]=="#" or maze_list[i-1][n]==" ":
                        j_num+=1
                    if maze_list[i][n+1]=="#" or maze_list[i][n+1]==" ":
                        j_num+=1
                    if maze_list[i+1][n]=="#" or maze_list[i+1][n]==" ":
                        j_num+=1
                    if j_num>2:
                        break_num+=1
                        maze_list[i][n]=" "
        if break_num==0:
            break
    for i in range(len(maze_list)):
        for n in range(len(maze_list[i])):
            if n==len(maze_list[i])-1:
                print(maze_list[i][n])
            else:
                print(maze_list[i][n],end="")



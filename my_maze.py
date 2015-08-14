__author__ = 'midorikawa'
import sys
"""
入力例
# ########
# #  ### #
#    ##  #
##      ##
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
"""
def make_maze(maze_list):
    for i in range(len(maze_list)):
        for j in range(len(maze_list[i])):
            if

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
                stop_num=0
                if maze_list[i][n]=="+" and i>0 and i<len(maze_list)-1 and n>0 and i<len(maze_list)-1:
                    if maze_list[i][n-1]=="#" or maze_list[i][n-1]==" ":
                        stop_num+=1
                    if maze_list[i-1][n]=="#" or maze_list[i-1][n]==" ":
                        stop_num+=1
                    if maze_list[i][n+1]=="#" or maze_list[i][n+1]==" ":
                        stop_num+=1
                    if maze_list[i+1][n]=="#" or maze_list[i+1][n]==" ":
                        stop_num+=1
                    if stop_num>2:
                        maze_list[i][n]=" "
                        break_num+=1
        if break_num==0:
            break
    for i in range(len(maze_list)):
        for n in range(len(maze_list[i])):
            if n==len(maze_list[i])-1:
                print(maze_list[i][n])
            else:
                print(maze_list[i][n],end="")
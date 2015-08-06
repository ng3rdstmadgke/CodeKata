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



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
maze_list=[]
for i in range(10):
    input=sys.stdin.readline().rstrip("\n")
    input_line=input.replace(" ","+")
    input_list=list(input_line)
    maze_list.append(input_list)


print(maze_list)
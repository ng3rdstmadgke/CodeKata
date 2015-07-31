__author__ = 'midorikawakeita'
import sys
def act_omoro(num):
    for i in range(1,num+1):
        if i%3==0:
            print("Aho",end=" ")
        elif str(i).count("3")!=0:
            print("Aho",end=" ")
        else:
            print(i,end=" ")

if __name__=="__main__":
    num=int(sys.stdin.readline())
    act_omoro(num)

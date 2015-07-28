__author__ = 'midorikawa.keita'
# -*- coding: utf-8 -*-

def my_lcg(n):
    x=12345
    list=[]
    for i in range(n):
        x=(997*x+1)%65536
        xx=x/100000
        list.append(xx)
    return list

if __name__=="__main__":
    xx=my_lcg(100)
    j=0
    for i in range(100):
        if i%10==0:
            print(xx[i])
        else:
            print(xx[i],end=" ")
        j+=xx[i]

    print("\n平均="+str(j/100))



__author__ = 'midorikawa.keita'
# -*- coding: utf-8 -*-

x=12345
j=0
for i in range(100):
    x=(997*x+1)%65536
    xx=x/100000
    print(xx)
    j+=xx

print("平均="+str(j/100))



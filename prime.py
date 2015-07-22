__author__ = 'le-user'
import sys
# -*- coding: utf-8 -*-
#input=sys.stdin.readline()
#n=int(input)
q=19
if pow(2,q-1,q)==1:
    print("True")
else:
    print("False")


list=range(2,n)
amari=[]
for i in list:
    amari.append(n%i)
for i in list:
    if(i == 0):
        print("is 0")
print(amari)
if 0 in amari==True:
    print("素数ではありません")
elif 0 in amari==False:
    print("素数です")
    """







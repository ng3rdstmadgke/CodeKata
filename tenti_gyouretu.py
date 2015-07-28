__author__ = 'midorikawa.keita'
import math
def input_line(input):
    list=input.split(" ")
    lines=math.sqrt(len(list))
    gyouretu=[]
    for i in range(lines):
        gyouretu+=list[i*0:i*lines]
    print(gyouretu)




list="1 2 3 4 5 6 7 8 9".split(" ")
print(list)
lines=int(math.sqrt(len(list)))
print(lines)
gyouretu=[]
for i in range(lines):
    gyouretu.append(list[i*3:(i+1)*3])
print(gyouretu)
print(gyouretu[1][2])
for i in range(3):
gyouretu[i]
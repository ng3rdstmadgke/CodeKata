__author__ = 'midorikawa.keita'
import math
def make_gyo(input):
    list=input.split(" ")
    lines=int(math.sqrt(len(list)))
    gyouretu=[]
    for i in range(lines):
        gyouretu.append(list[i*3:(i+1)*3])
    return gyouretu

def tenti_gyo(gyouretu):
    gyo_a=[]
    gyo_b=gyouretu
    n=len(gyouretu)
    for i in range(n):
        for j in range(n):
            gyo_a.append(gyo_b[j][i])
    return gyo_a


def print_gyo(list):
        for j in range(len(list)):
            if int(list[j])<10:
                print(" {} ".format(list[j]),end="")
            else:
                print("{} ".format(list[j]),end="")
            if (j+1)%(len(list)**0.5)==0:
                print("")

#if __name__=="__main__"
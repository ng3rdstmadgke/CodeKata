__author__ = 'midorikawa.keita'
import sys
#入力内容を行列の形式にする
def make_gyo(input):
    list=input.split(" ")
    lines=int((len(list))**0.5)
    gyouretu=[]
    for i in range(lines):
        gyouretu.append(list[i*lines:(i+1)*lines])
    return gyouretu

#受け取った行列を転置してリストで返す
def tenti_gyo(gyouretu):
    gyo_a=[]
    gyo_b=gyouretu
    n=len(gyouretu)
    for i in range(n):
        for j in range(n):
            gyo_a.append(gyo_b[j][i])
    return gyo_a

#出来上がった転置リストを行列の形式で表示
def print_gyo(list):
        for j in range(len(list)):
            if int(list[j])<10:
                print(" {} ".format(list[j]),end="")
            else:
                print("{} ".format(list[j]),end="")
            if (j+1)%(len(list)**0.5)==0:
                print("")


if __name__=="__main__":
    input_line=sys.stdin.readline()
    gyouretu=make_gyo(input_line)
    gyouretu_tenti=tenti_gyo(gyouretu)
    print_gyo(gyouretu_tenti)

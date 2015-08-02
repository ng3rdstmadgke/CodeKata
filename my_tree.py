__author__ = 'midorikawa'
import turtle
def my_tree(n,t):
    if n>10:
        #n進む
        t.fd(n)
        #３０度左に曲がる
        t.left(30)
        #n/2進む
        my_tree(n/2,t)
        #６０度右に曲がる
        t.right(60)
        my_tree(n/2,t)
        #n/2進む
        t.left(30)
        #n/2戻る
        t.fd(-n)

if __name__=="__main__":
    t=turtle.Turtle()
    t.goto(-400,0)
    my_tree(400,t)

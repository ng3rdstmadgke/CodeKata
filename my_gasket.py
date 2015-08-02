__author__ = 'midorikawa'
import turtle
def sankaku(n,t):
    for i in range(3):
        t.fd(n)
        t.left(120)
#    t.goto(n/4,(n/4)*(3**0.5))
#    for i in range(3):
#        t.fd(n/2)
#        t.right(120)

def go_point(x,y,t):
    t.penup()
    t.goto(x,y)
    t.pendown()

def gasket(n,length,t):
    if n>1:
        gasket(n-1,length,t)
        go_point(length*(n-2),0,t)
        t.fd(length*2**(n-1))
        gasket(n-1,length,t)
        go_point(length*(n-2),0,t)
        t.left(60)
        t.fd(length*2**(n-1))
        t.right(60)
        gasket(n-1,length,t)
    if n==1:
        sankaku(length,t)
        t.fd(length)
        sankaku(length,t)
        t.left(120)
        t.fd(length)
        t.right(120)
        sankaku(length,t)



if __name__=="__main__":
    t=turtle.Turtle()
    gasket(3,10,t)


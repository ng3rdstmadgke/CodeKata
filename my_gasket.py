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
    if n+1>0:
        gasket(n-1,length,t)
        go_point(length*2**n,0,t)
        gasket(n-1,length,t)
        go_point(length/2*n,length*n/2*(3**0.5),t)
        gasket(n-1,length,t)
        go_point(length*2**n,0,t)
    if n+1==0:
        sankaku(length,t)



if __name__=="__main__":
    t=turtle.Turtle()
    gasket(1,10,t)


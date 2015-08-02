__author__ = 'midorikawa'
import turtle
def sankaku(n,t):
    for i in range(3):
        t.fd(n)
        t.left(120)


def gasket(n,length,t):
    if n>1:
        gasket(n-1,length,t)
        t.fd(length)
        t.right(60)
        t.fd(length*2**(n-1)-length)
        t.left(60)
        gasket(n-1,length,t)
        t.left(60)
        t.fd(length)
        t.left(120)
        t.fd(length*2**(n-1))
        t.right(180)
        gasket(n-1,length,t)
    if n==1:
        for i in range(2):
            t.fd(length*2)
            t.left(120)
        t.fd(length)
        t.left(120)
        for i in range(2):
            t.fd(length)
            t.right(120)
        t.fd(length)
        t.left(120)
        t.fd(length)
        t.left(180)
        t.fd(length)
        t.right(60)




if __name__=="__main__":
    t=turtle.Turtle()
    gasket(5,10,t)


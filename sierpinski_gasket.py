__author__ = 'midorikawakeita'
import turtle

kame=turtle.Turtle()
run=150.0
turn=120.0
for i in range(3):
    kame.forward(run)
    kame.left(turn)
kame.forward(run/2)
kame.left(turn/2)

for i in range(3):
    kame.forward(run/2)
    kame.left(turn)

kame.right(turn/2)
kame.forward(run/4)
kame.left(turn/2)
for i in range(3):
    kame.forward(run/4)
    kame.left(turn)
kame.right(turn/2)


kame.forward(run/4)
kame.left(turn)
kame.forward(run*3/4)
for i in range(3):
    kame.forward(run/4)
    kame.left(turn)

kame.right(turn/2)
kame.forward(run/4)
kame.left(turn/2)
for i in range(3):
    kame.forward(run/4)
    kame.left(turn)
kame.right(turn/2)
input()

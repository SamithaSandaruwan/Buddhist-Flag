import time
from turtle import *
title("buddhist flag")
setup (800,600)
penup()
goto(-310,200)
pendown()
setheading(270)
colours=["blue","yellow","red","white","orange"]

for x in range(5):
    clr = colours[x]
    color(clr)
    begin_fill()
    forward(400)
    left(90)
    forward(100)
    left(90)
    forward(400)
    end_fill()
    right(180)
    end_fill()

penup()

setheading(360)
colours=["blue","yellow","red","white","orange"]

for x in range(5):
    clr = colours[x]
    color(clr)
    begin_fill()
    forward(100)
    right(90)
    forward(80)
    right(90)
    forward(100)
    end_fill()
    right(180)
    end_fill()


color("black")
pensize(10)
pendown()
forward(100)
left(90)
forward(400)
left(90)
forward(600)
left(90)
forward(400)
left(90)
forward(500)

time.sleep(7)

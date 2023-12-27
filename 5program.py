from turtle import *
import colorsys
tracer(100)
bgcolor('black')
h=0.1
pensize(4)

def fun():
    global h
    for i in range(4):
        c = colorsys.hsv_to_rgb(h,1,1)
        fillcolor(c)
        h+=0.004
        begin_fill()
        forward(50)
        right(20)
        forward(40)
        right(9)
        end_fill()
for j in range(300):
    fun()
    goto(0,0)
    right(10)
done()

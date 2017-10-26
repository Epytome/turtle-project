from turtle import *
import math
import random
jim = Turtle()
joe = Turtle()
hop = Turtle()
bob = Turtle()
jack = Turtle()
jill = Turtle()
jason = Turtle()
hop = Turtle()
bop = Turtle()
ast = Turtle()
colormode(255)
screensize(1000, 400)
all_turtles = (jim, joe, hop, bob, jack, jill, jason)

def draw_circle(t, x, y, line, radius,  fill):
    penup()
    goto(x, y)
    pendown()
    color(line, fill)
    circle(radius)
    
speed(10)






for i in range (1):
    draw_circle(jim ,0, 0, "red",100, "red")
    draw_circle(jim ,0, 0, "red",-100, "red")
    draw_circle(joe ,0, 0, "orange", 90,  "red")
    draw_circle(joe ,0, 0, "orange", -90,  "red")
    draw_circle(hop ,0, 0, "green", 80, "red")
    draw_circle(hop ,0, 0, "green", -80, "red")
    draw_circle(bob ,0, 0, "blue", 70, "red")
    draw_circle(bob ,0, 0, "blue", -70, "red")
    draw_circle(jack ,0, 0, "indigo", 60, "red")
    draw_circle(jack ,0, 0, "indigo", -60, "red")
    draw_circle(jill ,0, 0, "violet", 50, "red")
    draw_circle(jill ,0, 0, "violet", -50, "red")


clear()
reset()


def forward():
    bop.forward(20)

def right_key():
    bop.right(15)

def left_key():
    bop.left(15)

def back():
    bop.back(20)

def red():
    bop.color("red")
    
def green():
    bop.color("green")

def space_bar():
    if bop.isdown():
        bop.penup()

    else:
        bop.pendown()

def pen1():
    bop.pensize(1)

def pen2():
    bop.pensize(2)

def pen3():
    bop.pensize(3)

def pen4():
    bop.pensize(4)

def pen5():
    bop.pensize(5)

def pen6():
    bop.pensize(6)

def pen7():
    bop.pensize(7)

def pen8():
    bop.pensize(8)

def pen9():
    bop.pensize(9)

def pen10():
    bop.pensize(10)

def undo():
    bop.undo()

def circle():
    if bop.circle(50):
        bop.speed(10)
        



onkeypress(forward, "Up")
onkeypress(right_key, "Right")
onkeypress(left_key, "Left")
onkeypress(back, "Down")
onkeypress(red, "r")
onkeypress(green, "g")
onkeypress(space_bar, "space")
onkeypress(pen1, "1")
onkeypress(pen2, "2")
onkeypress(pen3, "3")
onkeypress(pen4, "4")
onkeypress(pen5, "5")
onkeypress(pen6, "6")
onkeypress(pen7, "7")
onkeypress(pen8, "8")
onkeypress(pen9, "9")
onkeypress(pen10, "0")
onkeypress(undo, "BackSpace")
onkeypress(circle, "o")

screen.onlcick(bop.goto)





        



listen()





done()

import turtle
t=turtle.Turtle()

def square(length) :
    for i in range(4) :
        t.forward(length)
        t.left(90)

def draw(x,y) :
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()
    
s=turtle.Screen()
s.onscreenclick(draw)

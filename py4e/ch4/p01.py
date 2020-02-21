import turtle
t=turtle.Turtle()

for count in range(6) : #6circle
    t.circle(100)
    t.left(360/6)

t.penup()
t.goto(200,0)
t.pendown()
s=turtle.textinput("","n각형 ")
n=int(s)
for i in range(n) :
    t.forward(100)
    t.left(360/n)

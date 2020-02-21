import turtle
t=turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(0,0)
t.pendown()
s=turtle.textinput("","Enter number ")
n=int(s)
if(n>0) :
    t.goto(100,100)
    t.write("+")
elif(n==0) :
    t.goto(100,0)
    t.write("0")
elif(n<0) :
    t.goto(100,-100)
    t.write("-")

import turtle
t=turtle.Turtle()
t.shape("turtle")
n=int(input("n각형 : "))

for i in range(n) :
    t.forward(100)
    t.left(360/n)

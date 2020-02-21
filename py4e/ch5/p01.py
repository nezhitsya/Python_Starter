import turtle
t=turtle.Turtle()

def n_polygon(n,length) :
    for i in range(n) :
        t.forward(length)
        t.left(360/n)
for i in range(10) :
    t.left(20)
    n_polygon(6,100)

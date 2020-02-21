import turtle
t=turtle.Turtle()
t.shape("turtle")
t.width(3)

while True :
    command=input("where to go(r/l)")
    if command=="l" :
        t.left(90)
        t.forward(100)
    if command=="r" :
        t.right(90)
        t.forward(100)

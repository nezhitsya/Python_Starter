import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput("","Enter ur name")
t.write("Hello"+s)

color_list=["yellow","red","blue","green"]
t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.forward(50)
t.pendown()

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()

import turtle
import random
t=turtle.Turtle()

def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
turtle.colormode(255)

for i in range(45):

    t.color(colors())
    t.forward(i)
    t.left(45)







turtle.exitonclick()

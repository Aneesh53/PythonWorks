import turtle

# Create turtle object
t = turtle.Turtle()
screen = turtle.Screen()
t.speed("fastest")
t.hideturtle()
def Screen(x,y):
    print({x},{y})


# Draw the circle
t.penup()
t.goto(0, 0)  # Move the turtle to the bottom center of the circle
t.pendown()
t.circle(60)

t.penup()
t.goto(0,0)
t.pendown()
t.color("Green")
t.begin_fill()
t.forward(300)
t.right(90)
t.forward(120)
t.right(90)
t.forward(600)
t.right(90)
t.forward(120)
t.end_fill()

t.penup()
t.goto(0,120)
t.pendown()
t.color("Orange")
t.begin_fill()
t.right(90)
t.forward(300)
t.left(90)
t.forward(120)
t.left(90)
t.forward(600)
t.left(90)
t.forward(120)
t.left(90)
t.forward(300)
t.end_fill()
screen.onclick(Screen)
t.penup()
t.goto(-300,0)
t.pendown()
t.color("black")
t.right(270)
t.forward(120)
t.penup()
t.goto(300,0)
t.pendown()
t.color("black")

t.forward(120)

t.penup()
t.goto(0,60)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(5)
t.end_fill()
t.pensize(3)

for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15.5)






turtle.done()


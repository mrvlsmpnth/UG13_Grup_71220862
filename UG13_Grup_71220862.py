import turtle
s = turtle.Screen()
t = turtle.Turtle()

t.width(10)
#M
t.left(90)
t.forward(100)
t.left(135)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(100)

#8
t.penup()
t.goto(10,30)
t.pendown()
t.circle(30)
t.penup()
t.goto(10,90)
t.pendown()
t.circle(30)

#6
t.penup()
t.goto(100,30)
t.pendown()
t.circle(30)
t.backward(60)
t.left(90)
t.circle(-90,45)

#2
t.penup()
t.goto(180,100)
t.pendown()
t.left(45)
t.forward(50)
t.right(90)
t.forward(100)
t.left(90)
t.forward(50)

#S
t.penup()
t.goto(350,100)
t.pendown()
t.right(180)
t.circle(40,180)

t.circle(-40,270)























s.exitonclick()
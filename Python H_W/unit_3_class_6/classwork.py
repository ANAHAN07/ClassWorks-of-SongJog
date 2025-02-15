import turtle

t = turtle.Turtle()
turtle.color("red")
turtle.speed(30)

for _ in range(3):
    t.forward(100)  
    t.left(120)  

t.penup()
t.forward(200)
t.pendown()

for _ in range(4):
    t.forward(150)
    t.right(90)


t.penup()
t.left(180)
t.forward(300)
t.pendown()


for _ in range(6):
    t.forward(150)
    t.right(60)

turtle.done()
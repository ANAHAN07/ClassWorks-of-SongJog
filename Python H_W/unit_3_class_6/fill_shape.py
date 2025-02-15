import turtle

turtle.speed(25)
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
for _ in range(6):
    turtle.forward(100)
    turtle.right(60)

turtle.end_fill()

turtle.done()
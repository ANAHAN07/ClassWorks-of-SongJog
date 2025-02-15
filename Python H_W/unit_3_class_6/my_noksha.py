import turtle
import random

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")  
turtle.colormode(255)  

for i in range(350):  
    t.pencolor(random_color())  
    t.width(i % 10 + 1)  
    t.forward(i * 2)  
    t.left(91)  
    t.circle(i // 3, 180)  

t.hideturtle()
turtle.done()
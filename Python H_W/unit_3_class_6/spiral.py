import turtle
import colorsys

turtle.speed(0)
turtle.bgcolor("black")
side_length = 10
num_lines = 100  
colors = [colorsys.hsv_to_rgb(i/num_lines, 1, 1) for i in range(num_lines)]

turtle.colormode(255) 
for i in range(num_lines):
    turtle.pencolor(int(colors[i][0] * 255), int(colors[i][1] * 255), int(colors[i][2] * 255))
    turtle.forward(side_length)
    turtle.right(60)
    side_length += 5 

turtle.done()
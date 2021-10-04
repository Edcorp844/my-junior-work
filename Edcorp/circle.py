import turtle
turtle.pensize(2)
turtle.speed(15)
turtle.bgcolor('black')

for i in range (15):
    for colors in ['yellow', 'green','purple','blue','pink','red','white']:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(10)
turtle.hideturtle()

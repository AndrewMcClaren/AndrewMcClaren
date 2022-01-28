import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.hideturtle()
lst = ["red","yellow","white","blue","cyan","green"]
for i in range(6):
    for color in lst:
        turtle.color(color)
        turtle.circle(60)
        turtle.left(10)

turtle.mainloop()
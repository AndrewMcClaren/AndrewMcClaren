import turtle as t

t.penup()
t.backward(120)
t.pendown()
t.speed(10)
t.hideturtle()
a = 200

for i in range(20):
    t.fd(a)
    t.left(120)
    a -= 10

for i in range(20):
    t.fd(a)
    t.left(120)
    a -= 10
t.mainloop()
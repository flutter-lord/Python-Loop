import random
import turtle as t
y = eval(input("Enter the value of y: "))
x = -y
z = y * 2

t.speed(4)
t.color("green")

for y in range(x, (y + 1), 10):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(z)

t.right(90)
for x in range(x, (y + 1), 10):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(z)

t.pensize(3)
t.color("red")

t.penup()
t.home()
t.pendown()
x = y = 0

t.speed(1)
while abs(x) < 80 and abs(y  < 80):
    r = random.randint(0, 3)
    if r == 0:
        x += 10

        t.setheading(0)
        t.forward(10)

    elif r == 1:
        y -= 10
        t.setheading(270)
        t.forward(10)

    elif r == 2:
        x -= 10
        t.setheading(180)
        t.forward(10)

    elif r == 3:
        y += 10
        t.setheading(90)
        t.forward(10)


t.done()
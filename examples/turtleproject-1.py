import turtle

a = turtle.Turtle(shape='turtle')
a.speed(0.5)

arka = turtle.getscreen()

arka.bgcolor("black")
a.color("blue")

a.up()
a.setposition(-80, -150)
a.down()

for i in range(50):
    a.circle(100)
    a.left(10)
    a.forward(50)
    a.circle(110)
    a.circle(120)
    a.circle(130)
    a.circle(140)
    a.circle(150)

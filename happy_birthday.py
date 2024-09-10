import turtle as jeetbanerjee

from turtle import *
from random import randint

jeet = jeetbanerjee.Screen()
jeet.bgcolor("black")
jeetbanerjee = jeetbanerjee.Turtle()
jeetbanerjee.width(7)
jeetbanerjee.shape('turtle')

colors = ["orange", "red", "dark blue", "green", "#fc037f", "gold", "ivory", "red", "pink",
          "green", "blue", "light green", ]


def draw_jeet(i, x, y):
    jeetbanerjee.pencolor("linen")
    jeetbanerjee.color(colors[i % 7])
    jeetbanerjee.begin_fill()
    jeetbanerjee.lt(70)
    jeetbanerjee.penup()
    jeetbanerjee.goto(x, y)
    jeetbanerjee.pendown()
    jeetbanerjee.circle(33)
    jeetbanerjee.end_fill()


def ballon(x, y):
    jeetbanerjee.pensize(1)
    for i in range(5):
        draw_jeet(i, x, y)


def cake(x, y):
    jeetbanerjee.fd(x)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(y)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(x)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(y)


def heart():
    for i in range(43):
        jeetbanerjee.pencolor(colors[i % 9])
        jeetbanerjee.rt(5)
        jeetbanerjee.fd(5)
    jeetbanerjee.pencolor("red")
    jeetbanerjee.fd(150)
    jeetbanerjee.penup()
    jeetbanerjee.rt(140)
    jeetbanerjee.fd(147)
    jeetbanerjee.pendown()
    for i in range(43):
        jeetbanerjee.pencolor(colors[i % 9])
        jeetbanerjee.lt(5)
        jeetbanerjee.fd(5)
    jeetbanerjee.pencolor("red")
    jeetbanerjee.lt(7)
    jeetbanerjee.fd(151)


def move(x, y):
    jeetbanerjee.up()
    jeetbanerjee.setposition(0, 0)
    jeetbanerjee.setheading(90)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(x)
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(y)
    jeetbanerjee.pendown()


def mov(x, y):
    jeetbanerjee.up()
    jeetbanerjee.setposition(0, 0)
    jeetbanerjee.setheading(90)
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(x)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(y)
    jeetbanerjee.pendown()


def A(size):
    jeetbanerjee.rt(15)
    jeetbanerjee.forward(size)
    jeetbanerjee.rt(150)
    jeetbanerjee.fd(size)
    jeetbanerjee.backward(size / 2)
    jeetbanerjee.rt(105)
    jeetbanerjee.fd(int(size / 3))


def B(size):
    jeetbanerjee.forward(size)
    jeetbanerjee.rt(90)
    for i in range(18):
        jeetbanerjee.rt(9)
        jeetbanerjee.fd(size // 20)
    for i in range(18):
        jeetbanerjee.rt(size // 5)
        jeetbanerjee.backward(size // 20)


def D(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 10)
    for i in range(13):
        jeetbanerjee.rt(13)
        jeetbanerjee.fd(size // 8)


def E(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.backward(size // 2)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.backward(size // 2)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(size // 2)


def G(size):
    jeetbanerjee.pensize(10)
    jeetbanerjee.penup()
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.pendown()
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(size // 4)
    jeetbanerjee.backward(size // 1.5)
    jeetbanerjee.lt(90)
    for _ in range(size):
        jeetbanerjee.rt(4)
        jeetbanerjee.fd(4)


def H(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.backward(size // 2)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.backward(size)


def I(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.rt(90)
    jeetbanerjee.circle(size // 8)


def K():
    jeetbanerjee.forward(60)
    jeetbanerjee.backward(30)
    jeetbanerjee.rt(45)
    jeetbanerjee.forward(42)
    jeetbanerjee.backward(42)
    jeetbanerjee.rt(90)
    jeetbanerjee.forward(42)


def N(size):
    jeetbanerjee.forward(size)
    jeetbanerjee.rt(150)
    jeetbanerjee.forward(size * 1.3)
    jeetbanerjee.lt(150)
    jeetbanerjee.forward(size)


def P(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 8)
    for i in range(8):
        jeetbanerjee.rt(20)
        jeetbanerjee.fd(size // 9)


def R():
    jeetbanerjee.fd(60)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(7)
    for i in range(15):
        jeetbanerjee.rt(12)
        jeetbanerjee.fd(3)
    jeetbanerjee.lt(120)
    jeetbanerjee.fd(40)


def S(size):
    jeetbanerjee.circle(size // 2, 180)
    jeetbanerjee.rt(180)
    jeetbanerjee.circle(size // 2, -180)


def T(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.backward(size // 2)


def U(size):
    jeetbanerjee.rt(90)
    for i in range(size // 10):
        jeetbanerjee.lt(15)
        jeetbanerjee.fd(size // 10)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.back(size // 2)

    for i in range(size // 10):
        jeetbanerjee.rt(13)
        jeetbanerjee.back(size // 10)
    jeetbanerjee.lt(5)
    for i in range(size // 10):
        jeetbanerjee.rt(17)
        jeetbanerjee.back(size // 10)
    jeetbanerjee.back(size // 2)


def Y(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.left(60)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.backward(size // 2)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 1.5)


def F(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.backward(size // 2)
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(size // 2)


def O(size):
    for i in range(36):
        jeetbanerjee.rt(10)
        jeetbanerjee.fd(size // 10)


def M(size):
    jeetbanerjee.fd(size)
    jeetbanerjee.rt(150)
    jeetbanerjee.fd(size * 1.3)
    jeetbanerjee.lt(150)
    jeetbanerjee.fd(size)


def J(size):
    jeetbanerjee.penup()
    jeetbanerjee.fd(size // 2)
    jeetbanerjee.pendown()
    jeetbanerjee.rt(90)
    jeetbanerjee.fd(size)
    jeetbanerjee.lt(90)
    jeetbanerjee.circle(-size // 4, 180)
    jeetbanerjee.lt(90)
    jeetbanerjee.fd(size // 2)


# Drawing section

jeetbanerjee.speed(19)
jeetbanerjee.width(5)

ballon(223, -150)
ballon(-233, -150)

mov(20, -130)
jeetbanerjee.width(13)

heart()

# Name section
jeetbanerjee.speed(40)
jeetbanerjee.width(4)
jeetbanerjee.pencolor("#7b30f2")

# SUKANYA
mov(230, 240)
S(size=60)
mov(190, 240)
U(60)
mov(150, 240)
K()
mov(110, 240)
A(size=60)
mov(70, 240)
N(60)
mov(30, 240)
Y(size=60)
mov(0, 240)  # Changed from -10 to 0 to move A more to the left
A(size=60)

# Space

# DEY
mov(-70, 240)  # Adjusted to maintain spacing after moving A
D(60)
mov(-110, 240)
E(60)
mov(-150, 240)
Y(60)

# (SUU)
mov(-190, 240)
jeetbanerjee.penup()
jeetbanerjee.write("(SUU)", font=("Arial", 24, "normal"))
jeetbanerjee.pendown()

# Cake maker section
jeetbanerjee.speed(3)
mov(120, 80)
jeetbanerjee.color("#94014b")
jeetbanerjee.begin_fill()
cake(40, 160)
jeetbanerjee.end_fill()
mov(110, 115)
jeetbanerjee.color("#fa348a")
jeetbanerjee.begin_fill()
cake(40, 140)
jeetbanerjee.end_fill()
mov(100, 150)
jeetbanerjee.color("#fa78b0")
jeetbanerjee.begin_fill()
cake(40, 120)
jeetbanerjee.end_fill()
mov(35, 200)
jeetbanerjee.width(11)
jeetbanerjee.pencolor("red")
jeetbanerjee.circle(7)

# Candles
jeetbanerjee.pensize(3)
jeetbanerjee.penup()
jeetbanerjee.goto(-100, 210)
jeetbanerjee.color("red")
jeetbanerjee.left(180)
jeetbanerjee.pendown()
jeetbanerjee.forward(20)

jeetbanerjee.penup()
jeetbanerjee.goto(-80, 210)
jeetbanerjee.color("orange")
jeetbanerjee.pendown()
jeetbanerjee.forward(20)

jeetbanerjee.penup()
jeetbanerjee.goto(-10, 210)
jeetbanerjee.color("orange")
jeetbanerjee.pendown()
jeetbanerjee.forward(20)

jeetbanerjee.penup()
jeetbanerjee.goto(20, 210)
jeetbanerjee.color("red")
jeetbanerjee.pendown()
jeetbanerjee.forward(20)

# End of Cake Section

# Happy Birthday
jeetbanerjee.pencolor("#4ceda2")
jeetbanerjee.width(13)
mov(260, -30)
H(100)
jeetbanerjee.width(7)
mov(190, -30)
A(65)
mov(135, -30)
P(60)
mov(100, -30)
P(60)
mov(52, -30)
Y(60)
mov(28, -30)
B(60)
move(12, -30)
I(60)
move(36, -30)
R()
move(80, -30)
T(100)
move(102, -30)
H(60)
move(150, -30)
jeetbanerjee.pencolor('hotpink')
D(200)
move(160, -30)
A(60)
move(220, -30)
Y(60)
jeet.exitonclick()
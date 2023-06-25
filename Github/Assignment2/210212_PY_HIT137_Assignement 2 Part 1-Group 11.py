from turtle import *
a = int(input("How many flowers would you like?: "))
ht()
pu()
goto(((a/2)*-400),0)
screensize((400*a)+400,600)
bgcolor("skyblue")
speed(50)
pd()
b = 1
for i in range (a):
    color("green","green")
    begin_fill()
    for i in range(1):
        forward(10)
        right(90)
        forward(250)
        left(135)
        circle(-80,90)
        right (90)
        circle (-80,90)
        left(135)
        forward(250)
        right(90)
        forward(20)
        right(90)
        forward(150)
        left(135)
        circle(-80,90)
        right (90)
        circle (-80,90)
        left(135)
        forward(350)
        right(90)
        forward(10)
    end_fill()
    if b == 1:
        c = "red"
    elif b == 2:
        c = "orange"
    elif b == 3:
        c = "yellow"
    elif b == 4:
        c = "green"
    elif b == 5:
        c = "blue"
    elif b == 6:
        c = "purple"
    elif b == 7:
        c = "indigo"
    else:
        b = 1
        c = "red"
    color(c, c)
    begin_fill()
    for i in range(6):
        circle(100)
        left(60)
    end_fill()
    color("white","white")
    begin_fill()
    b = b + 1
    for i in range(1):
        pu()
        setheading(270)
        forward(50)
        pd()
        setheading(0)
        circle(50)
        setheading(90)
        pu()
        forward(50)
        setheading(0)
        pd()
    end_fill()
    setheading(0)
    pu()
    forward(410)
    pd()
exitonclick()

from svg_turtle import SvgTurtle
import random



def createDraw():
    angle = random.randint(0, 360)
    print(angle)
    t = SvgTurtle(250,250)
    t.hideturtle()
    t.width(2)
    t.speed(10)
    t.color('blue')
    t.forward(100)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(angle)
    t.forward(100)

    t.goto(0, 0)
    t.penup
    t.dot(5, 'black')
    t.pendown()
    t.color('red')
    t.penup()

    t.goto(25, 0)
    t.pendown()
    t.setheading(90)
    t.circle(25, angle)

    t.save_as('drawing.svg')

    return angle
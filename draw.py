from svg_turtle import SvgTurtle
import random

# Cria a imagem do ângulo
def createDraw():
    # Declara um ângulo entre 0 e 360
    angle = random.randint(0, 360)
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
    t.penup()
    t.dot(5, 'black')
    t.pendown()
    t.color('red')
    t.penup()

    t.goto(25, 0)
    t.pendown()
    t.setheading(90)
    t.circle(25, angle)

    # Salva como .svg e retorna o ângulo
    t.save_as('drawing.svg')

    return angle
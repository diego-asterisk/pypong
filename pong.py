#!/usr/bin/env python3
import turtle

TOP = 290
BOTTOM = -290
LEFT = 390
RIGHT = -390

puntaje = {"jugador": 0, "adversario": 0}

ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(1, 6)

marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("{}\t\t{}".format(puntaje["jugador"], puntaje["adversario"]),
               align="center", font=("Curier", 24, "bold"))

jugador = turtle.Turtle()
jugador.speed(0)
jugador.shape("square")
jugador.color("cyan")
jugador.penup()
jugador.goto(-357, 0)
jugador.shapesize(stretch_wid=5, stretch_len=1)

adversario = turtle.Turtle()
adversario.speed(0)
adversario.shape("square")
adversario.color("white")
adversario.penup()
adversario.goto(357, 0)
adversario.shapesize(stretch_wid=5, stretch_len=1)

pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("yellow")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 3
pelota.dy = 3

red = turtle.Turtle()
red.color("grey")
red.goto(0, 400)
red.goto(0, -400)


def up(jugador):
    jugador.sety(jugador.ycor() + 20)


def down(jugador):
    jugador.sety(jugador.ycor() - 20)


def set_marca(puntaje):
    marcador.clear()
    msg = "{}\t\t{}".format(puntaje["jugador"], puntaje["adversario"])
    marcador.write(msg, align="center", font=("Curier", 24, "bold"))


def misma_altura(jugador, y):
    return y < jugador.ycor() + 50 and y > jugador.ycor() - 50


ventana.listen()
ventana.onkeypress(lambda: up(jugador), "w")
ventana.onkeypress(lambda: down(jugador), "s")
ventana.onkeypress(lambda: up(adversario), "Up")
ventana.onkeypress(lambda: down(adversario), "Down")

while True:
    ventana.update()
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    # rebote
    if pelota.ycor() > TOP:
        pelota.dy *= -1
    if pelota.ycor() < BOTTOM:
        pelota.dy *= -1
    # punto
    if pelota.xcor() > LEFT:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntaje["jugador"] += 1
        set_marca(puntaje)
    if pelota.xcor() < RIGHT:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntaje["adversario"] += 1
        set_marca(puntaje)
    # golpe
    y = pelota.ycor()
    x = pelota.xcor()
    if x > 340 and x < 350 and misma_altura(adversario, y):
        pelota.dx *= -1
    if x < -340 and x > -350 and misma_altura(jugador, y):
        pelota.dx *= -1

# Isto é uma demonstração do turtle
# Rodando no Python 2.7
# !!! match não funciona aqui !!!

from turtle import Turtle
turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("blue")
turtle.penup()
turtle.goto(-50, 100)
turtle.write("Python Base", None, "left", "12pt bold")
turtle.goto(-35, 70)
turtle.write("Linux Tips", None, "left", "12pt bold")
turtle.goto(-60, 30)
turtle.write("Clique em > Run", None, "left", "12pt bold")
turtle.goto(0, 0)

turtle.pendown()
turtle.circle(100)
turtle.penup()
import turtle
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

turtle_colors = ["red", "purple", "blue", "green","orange", "yellow"]


for i in range(1, 6):
    turtle_instance.color(random.choice(turtle_colors))
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)

turtle.done()
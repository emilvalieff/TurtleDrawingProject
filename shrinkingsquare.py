import turtle


turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    turtle_instance.penup()
    turtle_instance.goto(0, 0)
    turtle_instance.pendown()

    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5

shrinkingSquare(150)
shrinkingSquare(140)
shrinkingSquare(130)
shrinkingSquare(120)
shrinkingSquare(110)
shrinkingSquare(100)
shrinkingSquare(90)
shrinkingSquare(80)
shrinkingSquare(70)

turtle.done()

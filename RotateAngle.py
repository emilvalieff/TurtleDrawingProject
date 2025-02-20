import turtle


drawing_board = turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()


def turtle_forward():
    turtle_instance.forward(20)

def turtle_right():
    turtle_instance.right(20)

def turtle_left():
    turtle_instance.left(20)

def turtle_backward():
    turtle_instance.backward(20)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()

def pen_up():
    turtle_instance.penup()

def pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="Up")
drawing_board.onkey(fun=turtle_right, key="Right")
drawing_board.onkey(fun=turtle_left, key="Left")
drawing_board.onkey(fun=turtle_backward, key="Down")
drawing_board.onkey(fun=clear_screen, key="space")
drawing_board.onkey(fun=return_home, key="h")
drawing_board.onkey(fun=pen_up, key="q")
drawing_board.onkey(fun=pen_down, key="e")

turtle.mainloop()

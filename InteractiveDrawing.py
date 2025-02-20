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


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="w" )
drawing_board.onkey(fun=turtle_right, key="d" )
drawing_board.onkey(fun=turtle_left, key="a" )
drawing_board.onkey(fun=turtle_backward, key="s" )
turtle.mainloop()
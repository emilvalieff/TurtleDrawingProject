import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Python Turtle")


turtle_instance = turtle.Turtle()
for i in range(4):

    turtle_instance.forward(100)
    turtle_instance.right(90)
turtle.done()

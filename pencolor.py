import turtle
spiral=turtle.Turtle()
spiral.pencolor("blue")#changes the pen color
for i in range(50):
    spiral.forward(50)
    spiral.left(123)
spiral.pencolor("red")
for i in range(50):
    spiral.forward(100)
    spiral.left(123)
turtle.done()

import turtle
spiral=turtle.Turtle()
spiral.pencolor("blue")#changes the pen color
for i in range(20):
    spiral.forward(i*10)
    spiral.right(144)
spiral.pencolor("red")#changes the pen color
for i in range(20):
    spiral.forward(i*10)
    spiral.right(144)
turtle.done()

import turtle

screen = turtle.getscreen()
# turtle.bgcolor("black")
turtle.title("Turtle test drawings")

pencil = turtle.Turtle()
pencil.shape("circle")
pencil.shapesize(0.5, 0.5, 0.5)

startPointX = input("Set start x position: ")
startPointY = input("Set start y position: ")

x = int(startPointX)
y = int(startPointY)

pencil.speed(7)
pencil.up()
pencil.goto(x, y)
pencil.down()

pencil.speed(1)
pencil.right(100)
pencil.forward(200)

"""i = 100
while 1 > 10:
    pencil.circle(i)
    i -= 10
"""
turtle.exitonclick()
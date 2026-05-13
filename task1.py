import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numofsides=6
sidelength=70
angle=360/numofsides
polygon.fillcolor("blue")
polygon.begin_fill()
for i in range(numofsides):
    polygon.forward(sidelength)
    polygon.right(angle)
polygon.end_fill()
turtle.done()

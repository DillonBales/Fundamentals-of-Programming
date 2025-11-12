import turtle
wn = turtle.Screen() 
wn.bgcolor("purple")

leo = turtle.Turtle()

leo.speed(5)
leo.shape("turtle")
leo.pensize(3)
leo.color("pink")


for i in range(12):
    leo.penup()
    leo.forward(80)
    leo.pendown()
    leo.forward(15)
    leo.penup()
    leo.forward(15)
    leo.stamp()
    leo.left(180)
    leo.forward(110)
    leo.left(150)

leo.color("black")
leo.pensize(5)
leo.pendown()
leo.left(90)
leo.forward(70)
leo.left(180)
leo.forward(70)
leo.left(90)
leo.forward(50)
leo.left(180)
leo.forward(50)
leo.left(180)
leo.color("pink")


wn.mainloop() 
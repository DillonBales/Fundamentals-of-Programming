import turtle
wn = turtle.Screen() 
leo = turtle.Turtle()
wn.bgcolor("lightgreen")
leo.color("red")
leo.pensize(5)

def draw_star():
    for i in range(5):
        leo.right(144)
        leo.forward(100)

def draw_pattern():
    for i in range(5):
        draw_star()
        leo.penup()
        leo.right(144)
        leo.forward(350)
        leo.pendown()

draw_pattern()


wn.mainloop()

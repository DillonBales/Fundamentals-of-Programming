import turtle
wn = turtle.Screen() 
leo = turtle.Turtle()
wn.bgcolor("lightgreen")
leo.color("red")
leo.pensize(5)

def draw_square(size):
    for i in range(4):
        leo.forward(size)
        leo.left(90)

def draw_pattern(size):
    for i in range(5):
        draw_square(size)
        leo.right(135)
        leo.penup()
        leo.forward(14)
        leo.left(135)
        size = size + 20
        leo.pendown()

draw_pattern(20)



wn.mainloop()
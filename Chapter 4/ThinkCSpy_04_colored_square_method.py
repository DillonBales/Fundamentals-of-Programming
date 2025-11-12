import turtle
#__import__("turtle").__traceable__ = False

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

def draw_rectangle(t, w, h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square

for i in range(4):
    tess.pendown()
    draw_multicolor_square(tess, 50)
    tess.penup()
    tess.forward(100)
    tess.pendown()
    draw_multicolor_square(tess, 50)

    tess.penup()
    tess.right(90)
    tess.forward(100)
    tess.left(90)
    tess.pendown()
    draw_multicolor_square(tess, 50)

    tess.left(180)
    tess.penup()
    tess.forward(100)
    tess.left(180)
    tess.pendown()
    draw_multicolor_square(tess, 50)

    tess.right(90)
    tess.penup()
    tess.forward(100)
    tess.left(90)
    tess.pendown

    

wn.mainloop()
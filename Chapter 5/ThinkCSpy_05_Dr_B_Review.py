import turtle
import math

def make_window():
    w = turtle.Screen() # Set up the window and its attributes
    w.bgcolor("#E81727")
    w.title("Reviewing Functions")
    return w


def make_turtle(color:str, size:int):
    t = turtle.Turtle() # Create tess and set some attributes
    t.color(color)
    t.pensize(size)
    return t

def draw_triangle(t:turtle):
    t.pendown()# Make tess draw equilateral triangle
    for i in range(3):
      t.forward(80) 
      t.left(120)  
    t.penup() #get ready for the next thing

def draw_x(t:turtle):
    draw_triangle(tess)
    
    t.forward(20)
    
    draw_triangle(tess)
    
    t.forward(40)
    t.left(90)
    t.forward(80*math.cos(120))
    t.right(30)

    draw_triangle(tess)

    t.right(60)
    t.backward(20)
    t.left(60)

    draw_triangle(tess)


    t.backward(80)
    t.right(60)

def draw_pillar(t:turtle):
    draw_x(tess)
    t.right(90)
    t.forward(130)
    t.right(90)
    t.forward(80)
    t.right(180)
    draw_x(tess)
    t.forward(160)
    t.left(90)
    t.forward(5)
    t.right(90)
    draw_x(tess)

wn = make_window()
tess = make_turtle("#575351",5)

# tess.pendown()# Make tess draw equilateral triangle
# tess.forward(80) 
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120) # Complete the triangle
# tess.penup() #get ready for the next thing
# draw_triangle(tess)

# Move tess
# tess.forward(20)

# tess.pendown()# Make tess draw equilateral triangle
# tess.forward(80) 
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120) # Complete the triangle
# tess.penup() #get ready for the next thing
# draw_triangle(tess)

#move tess
# tess.forward(40)
# tess.left(90)
# tess.forward(80*math.cos(120))
# tess.right(30)

# tess.pendown()# Make tess draw equilateral triangle
# tess.forward(80) 
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120) # Complete the triangle
# tess.penup() #get ready for the next thing
# draw_triangle(tess)

#move tess
# tess.right(60)
# tess.backward(20)
# tess.left(60)

# tess.pendown()# Make tess draw equilateral triangle
# tess.forward(80) 
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120) # Complete the triangle
# tess.penup() #get ready for the next thing
# draw_triangle(tess)

#move tess
# tess.backward(80)
# tess.right(60)

draw_pillar(tess)

tess.hideturtle()
wn.mainloop()
import turtle
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle() # Create alex

for i in range(4):
    tess.forward(80) # Make tess draw equilateral triangle
    tess.left(120) # Complete the triangle

tess.right(180) # Turn tess around
tess.forward(80) # Move her away from the origin

for turn in [1, 2, 3, 4]:
    alex.forward(50) # Make alex draw a square
    alex.left(90)


wn.mainloop()
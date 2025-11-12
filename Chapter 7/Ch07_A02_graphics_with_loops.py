import turtle # Allows us to use turtles

def draw_zig_zag(w:turtle.Screen, t:turtle.Turtle):
    print("drawing zig zag")
    # # These variables might be helpful for you
    # left = -1 * w.canvwidth//2
    # right = w.canvheight //2
    # t.up() #lift the pen
    # t.goto(left , right)
    # t.setheading(0) #East (right)
    # t.down() #set the pen back down
    t.up()
    t.goto(-200, 200)
    t.down()
    for i in range(10):
        t.forward(400)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(400)
        t.left(90)
        t.forward(10)
        t.left(90)
    t.forward(400)


def draw_zz_down_and_up(w:turtle.Screen, t:turtle.Turtle):
    t.up()
    t.goto(-200, 200)
    t.down()
    for i in range(10):
        t.forward(150)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(150)
        t.left(90)
        t.forward(10)
        t.left(90)
    t.forward(400)

    for i in range(10):
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(150)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(150)
    

def draw_decreasing_spiral(w:turtle.Screen, t:turtle.Turtle):
    t.up()
    t.goto(-200, 200)
    t.down()
    length = 400
    while length > 0:
        t.forward(length)
        t.right(90)
        length = length - 10

def draw_spiral_in_and_out(w:turtle.Screen, t:turtle.Turtle):
    print("drawing the spiral in, then out")
    draw_decreasing_spiral(w,t)
    length = 10
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    while length < 400:
        length = length + 10
        t.forward(length)
        t.left(90)  



w = turtle.Screen() # Creates a playground for turtles
w.bgcolor("aqua")
t = turtle.Turtle() # Create a turtle, assign to alex
t.speed(0)


# draw_zig_zag(w,t)
# draw_zz_down_and_up(w,t)
# draw_decreasing_spiral(w,t)
draw_spiral_in_and_out(w,t)


w.mainloop() # Wait for user to close window
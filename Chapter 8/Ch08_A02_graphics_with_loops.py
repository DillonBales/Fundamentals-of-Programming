import turtle # Allows us to use turtles

def draw_zebra_stripes(w:turtle.Screen, t:turtle.Turtle):
    print("Starting zebra stripes")
    # These variables might be helpful for you
    left = -1 * w.canvwidth//2
    right = w.canvheight //2
    t.up() #lift the pen
    t.goto(left , right)
    t.setheading(270) #south (down)
    t.down() #set the pen back down
    

    for i in range(5):
        t.color("black")
        t.fillcolor("black")
        t.begin_fill()
        for i in range(2):
            t.forward(350)
            t.left(90)
            t.forward(40)
            t.left(90)
        t.end_fill()
        
        t.left(90)
        t.forward(40)
        t.right(90)
        
        t.color("white")
        t.fillcolor("white")
        t.begin_fill()
        for i in range(2):
            t.forward(350)
            t.left(90)
            t.forward(40)
            t.left(90)
        t.end_fill()

        t.left(90)
        t.forward(40)
        t.right(90)


def draw_jail_bird(w:turtle.Screen, t:turtle.Turtle):
    print("Starting Jail Bird")
    # These variables might be helpful for you
    left = -1 * w.canvwidth//2
    right = w.canvheight //2
    t.up() #lift the pen
    t.goto(left , right)
    t.setheading(270) #south (down)
    t.down() #set the pen back down
    

    for i in range(4):
        t.color("black")
        t.fillcolor("black")
        t.begin_fill()
        for i in range(2):
            t.forward(40)
            t.left(90)
            t.forward(350)
            t.left(90)
        t.end_fill()
        
        
        t.forward(40)
        
        
        t.color("white")
        t.fillcolor("white")
        t.begin_fill()
        for i in range(2):
            t.forward(40)
            t.left(90)
            t.forward(350)
            t.left(90)
        t.end_fill()

        
        t.forward(40)
        

def draw_squares(w:turtle.Screen, t:turtle.Turtle):
    print("Starting squares")
    # These variables might be helpful for you
    left = -1 * w.canvwidth//2
    right = w.canvheight //2
    t.up() #lift the pen
    t.goto(left , right)
    t.setheading(270) #south (down)
    t.down() #set the pen back down

    t.fillcolor("black")
    t.begin_fill()
    for i in range(4):
        t.forward(400)
        t.left(90)
    t.end_fill()

    t.left(45)
    t.forward(140)
    t.right(45)

    t.color("grey")
    t.fillcolor("grey")
    t.begin_fill()
    for i in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

    
    t.left(45)
    t.forward(70)
    t.right(45)

    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()





w = turtle.Screen() # Creates a playground for turtles
w.bgcolor("aqua")
t = turtle.Turtle() # Create a turtle, assign to alex
t.speed(0)



# draw_zebra_stripes(w,t)
# draw_jail_bird(w,t)
draw_squares(w,t)

w.mainloop() # Wait for user to close window
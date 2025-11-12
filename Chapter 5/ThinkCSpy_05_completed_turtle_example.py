import turtle

tess = turtle.Turtle()
wn = turtle.Screen()

xs = [48, 117, 200, 240, 160, 260, 220]

def draw_bar(t :turtle.Turtle, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill() # Added this line
    t.left(90)
    t.forward(height)     
    t.right(90)
    t.write(" "+ str(height))
    t.forward(40)         
    t.right(90) 
    t.forward(height)     
    t.left(90)            
    t.end_fill() # Added this line
    t.forward(10)         


for v in xs:              # Assume xs and tess are ready
    draw_bar(tess, v)


wn.mainloop() 
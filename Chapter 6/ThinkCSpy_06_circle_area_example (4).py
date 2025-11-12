import sys

def area_of_circle(): #currently a chatterbox function
    xc = input("Please enter the value for xc")
    yc = input("Please enter the value for yc")
    xp = input("Please enter the value for xp")
    yp = input("Please enter the value for yp")
    radius = pythagorean_theorem(xc, yc, xp, yp)
    result = area(radius)
    print ("The total area is: " + str(result))
    
def area(radius):
    return 3.14159 * radius * radius

def pythagorean_theorem(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test passed".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

print("Testing pythagorean_theorem")
test(pythagorean_theorem(1,2,4,6) == 5.0)
print("Should like test area (Dr. B. didn't write any tests)")

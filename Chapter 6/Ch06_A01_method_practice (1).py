import sys

def turn_clockwise(direction):
    if direction == "N":
        return "E"
    if direction == "E":
        return "S"
    if direction == "S":
        return "W"
    if direction == "W":
        return "N"


def day_name(number):
    if number == 0:
        return "Sunday"
    if number == 1:
        return "Monday"
    if number == 2:
        return "Tuesday"
    if number == 3:
        return "Wednesday"
    if number == 4:
        return "Thursday"
    if number == 5: 
        return "Friday"
    if number == 6:
        return "Saturday"

def day_num(name):
    if name == "Sunday":
        return 0 
    if name == "Monday":
        return 1
    if name == "Tuesday":
        return 2
    if name == "Wednesday":
        return 3
    if name == "Thursday":
        return 4
    if name == "Friday":
        return 5
    if name == "Saturday":
        return 6
    
def mysum(xs):
    total = 0
    for i in xs:
        total = total + i
    return total


     

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("E") == "S")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

    test(day_num("Sunday") == 0)
    test(day_num("Friday") == 5)
    test(day_num("Halloween") == None)

    test(mysum([1, 2, 3, 4]) == 10)

test_suite()
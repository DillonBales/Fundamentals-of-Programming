import sys

def sum_to(n):
    sum = 0
    v = 1
    while v <= n:
        sum = sum + v
        v = v + 1
    return sum 

def seq3np1(n):
    count = 0
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        count = count + 1

    print(n, end=".\n")

    print(count)

seq3np1(27)

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# test(sum_to(5) == )

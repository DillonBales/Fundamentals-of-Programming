import sys

def days_in_month(month):
    if month == "January":
        return 31
    if month == "February":
        return 28
    if month == "March":
        return 31
    if month == "April":
        return 30
    if month == "May":
        return 31
    if month == "June":
        return 30
    if month == "July":
        return 31
    if month == "August":
        return 31
    if month == "September":
        return 30
    if month == "October":
        return 31
    if month == "November":
        return 30
    if month == "December":
        return 31
    

def to_secs(hours, minutes, seconds):
    hour_sec = hours * 3600
    minute_sec = minutes * 60
    total = hour_sec + minute_sec + seconds
    return total


def compare(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0
    

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
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("January") == 31)
    test(days_in_month("March") == 31)
    test(days_in_month("April") == 30)
    test(days_in_month("May") == 31)
    test(days_in_month("June") == 30)
    test(days_in_month("July") == 31)
    test(days_in_month("August") == 31)
    test(days_in_month("September") == 30)
    test(days_in_month("October") == 31)
    test(days_in_month("November") == 30)


    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(0, 1, 0) == 60)
    test(to_secs(0, 0, 50) == 50)
    test(to_secs(1, 0, 0) == 3600)
    test(to_secs(50, 0, 0) == 180000)
    test(to_secs(10, 0, 35) == 36035)

    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(compare(17, 2) == 1)
    test(compare(2, 17) == -1)
    test(compare(-17, 2) == -1)
    test(compare(2, -17) == 1)
    test(compare(17, 17) == 0)
    


test_suite()
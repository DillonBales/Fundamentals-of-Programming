def star_pattern_1():
    pattern = "" 
    for i in range(20):
        pattern = pattern + "*"
        print(pattern)

def star_pattern_2():
    pattern = "********************"

    for i in range(20):
        pattern = pattern[1:]
        print(pattern)
    

def star_pattern_3():
    pattern = "********************"

    for i in range(20):
        print("{0:>20}".format(pattern))
        pattern = pattern[1:]


def star_pattern_4():
    pattern = "" 
    for i in range(20):
        pattern = pattern + "*"
        print("{0:>20}".format(pattern))

def star_pattern_5():
    pattern = "*" 
    for i in range(9):
        print("{0:^21}".format(pattern))
        pattern = pattern + "**"
    for a in range(10):
        print("{0:^21}".format(pattern))
        pattern = pattern[2:]

def print_patterns():
    star_pattern_1()
    print("")
    star_pattern_2()
    print("")
    star_pattern_3()
    print("")
    star_pattern_4()
    print("")
    star_pattern_5()



star_pattern_5()





# pattern = "********************"

# for a in range(20):
#     pattern = pattern[1:]
#     print(pattern)

pattern = "*"

# 19 stars 
for i in range(9):
        print("{0:^19}".format(pattern))
        pattern = pattern + "**"
for a in range(10):
    print("{0:^19}".format(pattern))
    pattern = pattern[2:]

# 17 stars
# for i in range(8):
#     print("{0:^17}".format(pattern))
#     pattern = pattern + "**"
# for a in range(9):
#     print("{0:^17}".format(pattern))
#     pattern = pattern[2:]

#15 stars
# for i in range(7):
#     print("{0:^21}".format(pattern))
#     pattern = pattern + "**"
# for a in range(8):
#     print("{0:^21}".format(pattern))
#     pattern = pattern[2:]

# def diamond():
#     answer = input("How many stars would you like in the largest row? ")
#     answer = float(answer)
#     range_1 = int((answer / 2) - 0.5)
#     range_2 = int((answer / 2) + 0.5)
#     pattern = "*" 
#     for i in range(range_1):
#         print("{0:^21}".format(pattern))
#         pattern = pattern + "**"
#     for a in range(range_2):
#         print("{0:^21}".format(pattern))
#         pattern = pattern[2:]

# diamond()
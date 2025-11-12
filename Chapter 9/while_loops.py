def something_in_the_90s():
    answer = input("Guess an integer between 1 and 100: ")
    while int(answer) >= 100 or int(answer) <= 89:
        answer = input("Incorrect, try again: ")
    print("Correct!")
    return answer

def something_in_the_negative_50s():
    answer = input("Guess an integer between -100 and 0: ")
    while int(answer) >= -49 or int(answer) <= -60 :
        answer = input("Incorrect, try again: ")
    print("Correct!")
    return answer

def something_larger_or_smaller():
    answer = input("Guess an integer outside the rang of 0 and 5: ")
    while int(answer) >= 0 and int(answer) <= 5 :
        answer = input("Incorrect, try again: ")
    print("Correct!")
    return answer  

def exactly_12345():
    answer = input("Guess an integer between -1,000,000 and 1,000,000: ")
    while int(answer) != 12345:
        answer = input("Incorrect, try again: ")
    print("Correct!")
    return answer   

def stars_going_down():
    answer = input("How many stars would you like in the largest row? ")
    pattern = "" 
    for i in range(int(answer)):
        pattern = pattern + "*"
        print(pattern)

def diamond():
    answer = input("How many stars would you like in the largest row? ")
    answer = float(answer)
    range_1 = int((answer / 2) - 0.5)
    range_2 = int((answer / 2) + 0.5)
    
    pattern = "*" 
    for i in range(range_1):
        print("{0:^{spacing}}".format(pattern, spacing = int(float(answer))))
        pattern = pattern + "**"
    for a in range(range_2):
        print("{0:^{spacing}}".format(pattern, spacing = int(float(answer))))
        pattern = pattern[2:]

something_in_the_90s()
something_in_the_negative_50s()
something_larger_or_smaller()
something_larger_or_smaller()
exactly_12345()
stars_going_down()
diamond()

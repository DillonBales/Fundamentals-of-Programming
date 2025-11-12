import random
#This method should return the number, one greater, than the one provided
#0 points
#For example, if the number provided was 4, the method should return 5
#
def give_me_the_next_number(a):
    return a+1 #I assume you will delete/replace this line

# This method should return True if the answer matches the user's guess, and False otherwise
# 5 points
def did_the_user_answer_this_correctly(answer, usersGuess):
    if answer == usersGuess:
        return True
    else:
        return False   #I assume you will delete/replace this line

# This method should return True if b is half of a, or False otherwise
# 10 points
# Examples:
#    the method should return true if the numbers provided are 8 and 4
#    the method should return false if the numbers provided are 9 and 4
#
#    You might need to watch out for this: 9 // 2 = 4 in integer division
#    To solve this potential problem, odd numbers could automatically be filtered to return false 
def is_b_half_of_a(a, b):
    if a/2 == b:
        return True
    else:
        return False
     #I assume you will delete/replace this line

# This method should determines if any of the integers are even
# 15 points
# Examples:
#  The method should return true for the following areAnyOneOfTheseVariablesEven(2,4,6,8)
#  The method should return true for the following areAnyOneOfTheseVariablesEven(1,3,5,100)
#  The method should return false for the following areAnyOneOfTheseVariablesEven(1,3,5,7)

def are_any_one_of_these_variables_even(a, b, c, d):
    if a%2 == 0:
        return True
    elif b%2 == 0:
        return True
    elif c%2 == 0:
        return True
    elif d%2 == 0:
        return True
    else:
        return False

# This method should searche through a list for the word Harry
# 15 points
# Example:  This list has the word Harry
#  ["Hello", "Harry"]
#  This list does not
#  ["No", "Strange", "Word", "Here"]
def contains_the_word_harry(a):
    for i in range(len(a)):
        if a[i] == "Harry":
            return True
    return False



# This method should return a string that contains the number provided, stuck together with itself 57 times
# 15 points
# Exmple
#   if the number 10 was provided, your method should return
#   "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"

def i_want_57_of_these_in_a_string(a):
    return str(a) * 57 #I assume you will delete/replace this line

# This method should look through the tuple and returns the first number less than 100 
# 20 points
#  Examples:
#  The number 1 should be returned from this tuple (1, 2, 3, 4, 5, 6)
#  The number 15 should be returned from this tuple (101, 456, 543, 15, 92, 1, 2, 3)
def first_number_below_100(a):
    for i in range(len(a)):
        if a[i] < 100:
            return a[i]



# This method should ask the following question exactly like it appears
# '''Which pet do you like? 1 for fish, 2 for cat, or 3 for dog: '''
# 20 points

# Your method should print the following based on what the user enters
# "I agree, fish are the best pets"
# "Cat's sure are nice"
# "Dogs sure are playful"
# If the user enter's any other number your method should print
# "I don't know that pet"
def ask_about_pets():
    answer = input('''Which pet do you like? 1 for fish, 2 for cat, or 3 for dog: ''')
    if answer == "1":
        print("I agree, fish are the best pets")
    elif answer == "2":
        print("Cat's sure are nice")
    elif answer == "3":
        print("Dogs sure are playful")
    else:
        print("I don't know that pet")




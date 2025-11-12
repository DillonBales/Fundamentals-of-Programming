# Practice on methods that uses lists

def getting_to_know_you(questions):
    print("Please answer the following questions:")
    answer_list = []
    for i in range(len(questions)):
        print(questions[i])
        answer = input()
        answer_list.append(answer)
    return answer_list


def print_question_with_answer(questions, answers):
     print("\nThe following are those questions, and your answers")
     #print("For example")
     #print("Are you in CS 1400 with Dr B? Yes I am")
     for i in range(len(questions)):
         print(questions[i])
         print(answers[i]) 

def more_getting_to_know_you(questions):
    print("\nPlease answer the following questions using only a y or n")
    answer_list = []
    for i in range(len(questions)):
        print(questions[i])
        answer = input()
        if answer == "y":
            answer = True
        else:
            answer = False
        answer_list.append(answer)
    return answer_list

def print_question_with_true_answer(questions, answers):
    print("\nThe following are questions you answered true to")
    for i in range(len(questions)):
        if answers[i] == True:
            print(questions[i])

def print_question_with_false_answer(questions, answers):
    print("\nThe following are questions you answered false to")
    for i in range(len(questions)):
        if answers[i] == False:
            print(questions[i])

questions = ["What makes you laugh the most?", "Who is your hero?", "If you could only eat one meal for the rest of your life, what would it be?", "Would you rather ride a bike, ride a horse, or drive a car?", "What did you want to be when you were small?", "What really makes you angry?", "What was your favorite vacation?", "How many pairs of shoes do you own?" ]
answers = getting_to_know_you(questions)
print_question_with_answer(questions, answers)

moreQuestions = ["Do you enjoy going to school?", "Have you ever burried a time capsule?", "Do you have a secret tallent?", "Do you belive in aliens?", "Do you have a sister or brother?", "Are you afraid of small spaces?", "Can you speak another language?", "Have you even met a celebrity?"]
moreAnswers = more_getting_to_know_you(moreQuestions)
print_question_with_true_answer(moreQuestions,moreAnswers)
print_question_with_false_answer(moreQuestions,moreAnswers)



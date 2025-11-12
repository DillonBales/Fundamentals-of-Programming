grade = input("Enter you numerical grade: ")

grade = int(float(grade))

if 100 >= grade >= 94:
    grade = "A"
elif 94 > grade >= 90:
    grade = "A-"
elif 90 > grade >= 87:
    grade = "B+"
elif 87 > grade >= 84:
    grade = "B"
elif 84 > grade >= 80:
    grade = "B-"
elif 80 > grade >= 77:
    grade = "C+"
elif 77 > grade >= 74:
    grade = "C"
elif 74 > grade >= 70:
    grade = "C-"
elif 70 > grade >= 67:
    grade = "D+"
elif 67 > grade >= 64:
    grade = "D"
elif 64 > grade >= 61:
    grade = "D-"
elif 61 > grade >= 0:
    grade = "F"
else:
    print("Invalid Input")

print("Your letter grade is a(n)", grade + ".")
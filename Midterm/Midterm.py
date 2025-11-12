# Name: Dillon Bales

print("Welcome to the Bank of Barker")
name = input("Please enter your first name: ")
years = input("Please enter the number of years you like to loan: ")
amount = input("Please enter the amount for your loan: ")
print("For you", name, "we have the following deal")
years = int(years)
amount = int(amount)

if (years) >= 30:
    interest = 15
elif years < 30 or years >= 10:
    interest = 10
elif years < 10 or years >= 5:
    interest = 5
elif years < 5:
    interest = 2
else:
    print("Invalid year input")

print("For a loan amount of", amount, "we can provide you and interest rate of", str(interest) + "%")

total = amount + (amount * (interest * 0.01))

print("the total, with interest, will be $" + str(total))


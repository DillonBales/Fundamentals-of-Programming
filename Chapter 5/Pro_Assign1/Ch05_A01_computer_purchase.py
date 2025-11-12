print("Welcome to Barker's Computer Store.  I can help you purchase a computer")
print("Would you like the basic computer model (costing $375.99) or the advanced model optimized for computer programming (costing $775.99)?")
computer = input('Enter either "Basic" or "Advanced": ')
print("Would you like the 38 cm screen (costing $75.99) or the 43 cm screen (costing $99.99)")
monitor = input('Enter either "38" or "43": ')
print("Would you like Antivirus software (costing $65.99)")
anti = input("Yes or No: ")
print("Would you like Printer (costing $125.00)")
printer = input("Yes or No: ")
print("Would you like Webcam (costing $599.99 due to supply chain issues or basic price gouging)")
webcam = input("Yes or No: ")

if computer.upper() == "BASIC":
    computer = 375.99
elif computer.upper() == "ADVANCED":
    computer = 775.99
else:
    print("Invalid Input")
    
if monitor == "38":
    monitor = 75.99
elif monitor == "43":
    monitor = 99.99
else: 
    print("Invalid Input")

if anti.upper() == "YES":
    anti = 65.99
elif anti.upper() == "NO":
    anti = 0
else:
    print("Invalid Input")

if printer.upper() == "YES":
    printer = 125
elif printer.upper() == "NO":
    printer = 0
else:
    print("Invalid Input")
    
if webcam.upper() == "YES":
    webcam = 599.99
elif webcam.upper() == "NO":
    webcam = 0
else:
    print("Invalid Input")

total = computer + monitor + anti + printer + webcam

print("Your total is: $" + total)


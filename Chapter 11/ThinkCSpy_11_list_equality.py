a = [1,2,3]
b = [1,2,3]
x = input("Please type 1: ")
y = input("Please type 2: ")
z = input("Please type 3: ")
c = [x,y,z]

if a == b:
    print("a == b")
else:
    print("not a == b")

if a == c:
    print("a == c")
else:
    print("not a == c")

if a is b:
    print("a is b")
else:
    print("not a is b")

if a is c:
    print("a is c")
else:
    print("not a is c")

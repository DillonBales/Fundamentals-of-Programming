fruit = "banana"

print(list(enumerate(fruit)))

for c in fruit:
    print(c)

print("\b")

for i in range(len(fruit)):
    print(fruit[i])

friends = ["Joe", "Jim", "Zoe", "Brad", "Paris"]
print(friends[2:4]) 
#the indexes are the spaces between the letters. 

print(fruit[:3])
print(fruit[3:])

greeting = "Hello World"
print("J" + greeting[1:])

if "a" in "a":
    print("True")
if "apple" in "apple":
    print("True")

if "x" not in "apple":
    print("True")

if not "x" in "apple":
    print("True")

s = "hello world"
vowels = "aeiouAEIOU"
s_sans_vowels = ""
for i in s:
    if i not in s:
        s_sans_vowels += i


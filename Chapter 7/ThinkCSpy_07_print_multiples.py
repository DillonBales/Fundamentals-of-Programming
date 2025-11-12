def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()

def print_multiplication_table(n):
    for i in range(1, 7):
        print_multiples(i)

print_multiplication_table(6)
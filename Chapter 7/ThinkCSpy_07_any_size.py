def print_multiples(n, max):
    for i in range(1, max + 1):
        print(n * i, end="\t")
    print()

def print_multiplication_table(max):
    for i in range(1, max + 1):
        print_multiples(i, max)

print_multiplication_table(15)
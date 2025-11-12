

def distance(first_x, second_x, first_y, second_y):
    dx = second_x - first_x
    dy = second_y - first_y

    sum_square = dx ** 2 + dy **2

    return sum_square**0.5

def midpoint(first_x, second_x, first_y, second_y):
    mx = (first_x + second_x) / 2
    my = (first_y + second_y) / 2

    return mx, my

x_1 = float(input("Enter First x Quordinate: "))
x_2 = float(input("Enter Second x Quordinate: "))
y_1 = float(input("Enter First y Quordinate: "))
y_2 = float(input("Enter Second y Quordinate: "))

print("Distance is:", distance(x_1, x_2, y_1, y_2))
print("Midpoint is:", midpoint(x_1, x_2, y_1, y_2))
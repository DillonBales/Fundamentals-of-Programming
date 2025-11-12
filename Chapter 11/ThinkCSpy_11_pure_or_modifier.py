def double_stuff(a_list):
    new_list = []
    for i in range(len(a_list)):
        new_elm = 2 * a_list[i]
        new_list.append(new_elm)
    return new_list

things = [2, 5, 9]
second = double_stuff(things)
print(things)
print(second)




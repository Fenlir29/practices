my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

for odd in range(len(my_list)-1, -1,-1):
    if my_list[odd] % 2 == 1:
        delete_odd = my_list.pop(odd)
print(my_list)



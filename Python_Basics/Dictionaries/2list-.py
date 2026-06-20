list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

my_list = {}
for index in range(len(list_a)):
    my_list[list_a[index]] = list_b[index]



print(my_list)
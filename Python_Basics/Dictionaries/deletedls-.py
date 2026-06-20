list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for key in list_of_keys:
    if key in employee:
                deleted_item = employee.pop(key)

print(employee)


# for key in employee.keys():
#     if key in list_of_keys:
#         deleted_item = employee.pop(key)

# print(employee)


# for key in list(employee.keys()):
#     if key in list_of_keys:
#         deleted_item = employee.pop(key)

# print(employee)



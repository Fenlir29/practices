numbers = []
highest_number = 0


print("ingrese 10 numeros:")
for i in range(0,10):
    user_input = int(input("siguiente numero:"))
    numbers.append(user_input)
    if highest_number < user_input:
        highest_number = user_input

print(f"{numbers} El numero mayor es:{highest_number}")
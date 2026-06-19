
greater_number = int(input("Ingrese numero: "))

for minor_number in range(2):
    minor_number = int(input("Siguiente numero: "))
    if (greater_number < minor_number):
        greater_number = minor_number
print(f"El numero mayor es {greater_number}")


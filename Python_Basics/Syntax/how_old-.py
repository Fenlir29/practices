print("Bienvenido averiguamos que tan viejo eres")
full_name = input("Cual es tu nombre y apellido ?\n")
age = int(input("ingresa tu edad: "))

if age <= 3:
    category = "Bebe" 
elif age <= 9:
    category = "Niño"
elif age <= 14:
        category = "preadolescente"
elif age <= 17:
        category = "adolescente"
elif age <= 24:
        category = "adulto joven"
elif age <= 79:
        category = "adulto"
else:
    category = "adulto mayor" 

print(f"{full_name} es considerado un {category} de {age} años")


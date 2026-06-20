time_s = int(input("ingrese tiempo en segundos:"))
if time_s < 600:
    remaining_time = 600 - time_s
    print(f"faltan {remaining_time} segundos para llegar a 10 minutos.")
elif time_s > 600:
    print("El valor ingresado es mayor a 10 minutos")
else:
    print("el valor es igual a 10 minutos ")
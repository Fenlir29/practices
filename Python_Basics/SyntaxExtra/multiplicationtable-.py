multiplier = 1
numberformultiply = int(input("ingrese un numero del 1 al 10:"))

while numberformultiply > 10 or numberformultiply <= 0:
    numberformultiply = int(input("Valor invalido intente otra vez"))
for i in range(12):
    total_multiply = numberformultiply * multiplier
    print(f"{numberformultiply} x {multiplier} = {total_multiply}")
    multiplier += 1
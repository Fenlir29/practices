import random

secret_number = random.randint(1,10)
print("Adivina el numero del 1 al 10:")
while True:
    user_guess = int(input())
    if user_guess == secret_number :
        print("\n" "Ganaste!!!")
        break
    print("\n" "intenta otra vez:")
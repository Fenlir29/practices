def add(num1,num2):
    return num1 + num2 

def subtract(num1,num2):
    return num1 - num2 

def multiply(num1,num2):
    return num1 * num2 

def division(num1,num2):
    try:
        return num1 / num2 
    except ZeroDivisionError as error:
        print(f"{error}")
        return 0


def menu(num1):
    print("-----Calculadora-----")
    print(f"Resultado actual:{num1}")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Borrar")
    print("6.Salir")


def calculator():
    num1 = 0
    num2 = 0
    while True:
        menu(num1)
        
        option = input(":")
        if option not in ["1","2","3","4","5","6"]:
            print("opcion invalida")
        elif option in ["1", "2", "3", "4"] and num1 != 0:
            try:
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError as error:
                print(f"caracter invalido:{error}")
                num2 = 0
        elif num1 == 0 and option != "6":
            try:
                num1 = float(input("ingrese primer numero:"))
                num2 = float(input("ingrese segundo numero:"))
            except ValueError as error:
                print(f"caracter invalido:{error}")
                num1 = 0
                num2 = 0

        elif option == "6":
            print("Hasta pronto")
            break

        if option == "1":
            num1 = add(num1,num2)
            print("Resultado:",num1)
        elif option == "2":
            num1 = subtract(num1,num2)
            print("Resultado:",num1)
        elif option == "3":
            num1 = multiply(num1,num2)
            print("Resultado:",num1)
        elif option == "4":
            num1 = division(num1,num2)
            print("Resultado:",num1)
        

        if option == "5":
            num1 = 0

def main():
    try:
        calculator()
    except Exception as ex:
        print(f"Error inesperado: {ex}")


main()
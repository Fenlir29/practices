def printMm(text):
    isupper = 0
    islower = 0
    for character in text:
        if character.isupper():
            isupper += 1
        elif character.islower():
            islower += 1
    print(f"Mayusculas:{isupper} minusculas:{islower}")

def main():
        text = input("Ingrese frase: ")
        (printMm(text))


main()

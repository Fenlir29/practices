def sort_bya(words):
    words = words.split("-")
    text = sorted(words)
    result = "-".join(text)
    return result

def main():
    words = input("ingrese palabras separadas por - :")
    print(sort_bya(words))


main()
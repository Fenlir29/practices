import csv

def csvfile(file_name,data):
    try:
        with open(file_name,'x') as f:
            pass
        file_exists = False
    except FileExistsError:
        file_exists = True
    with open(file_name,'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='\t') 
        if not file_exists:
            writer.writerow((['nombre', 'genero', 'desarrollador', 'clasificacion']))

        for games in data:
            writer.writerow(games)




def get_data():
    games = []

    n = int(input("Cuantos juegos quiere guardar?"))

    for i in range(1 ,n + 1):
        print(f"juego {i}")

        name = input("Nombre: ")
        genre = input("Género: ")
        developer = input("Desarrollador: ")
        ranking = input("Clasificación ESRB: ")

        games.append([name,genre,developer,ranking])
    return games
        

def main():
    file_name = "games.csv"
    data = get_data()
    csvfile(file_name, data)


main()
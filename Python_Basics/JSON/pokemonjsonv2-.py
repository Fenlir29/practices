import json



def checkpk(file_name):
    with open(file_name, 'r', encoding='utf-8') as pokemons:
        data = json.load(pokemons)
        
        print("\n=== POKÉMONES REGISTRADOS ===")
        
        for pokemon in data:
            print(f"\nNombre: {pokemon['name']}")
    
    return data

def save(file_name, all_pokemons):
    with open(file_name, 'w', encoding='utf-8') as save_file:
        json.dump(all_pokemons, save_file, indent=4)
    print("\n✅ Pokémon guardado exitosamente!")

def get_pokemon():
    skills_list = []
    print("\n=== NUEVO POKÉMON ===")
    print("Ingrese los datos del nuevo Pokémon:")
    
    name = input("Nombre: ")
    typ = input("Tipo: ")
    level = int(input("Nivel: "))
    weight = float(input("Peso (kg): "))
    shiny = input("¿Es shiny? (si/no): ").lower() == "si"
    
    held_item = input("Objeto equipado (deje vacío si no tiene): ")
    if held_item == "":
        held_item = None
    
    print("\nIngrese 4 habilidades:")
    for i in range(4):
        skill = input(f"Habilidad {i + 1}: ")
        skills_list.append(skill)
    
    print("\nIngrese las estadísticas:")
    stats = {
        "hp": int(input("HP: ")),
        "attack": int(input("Ataque: ")),
        "defense": int(input("Defensa: ")),
        "sp_attack": int(input("Ataque especial: ")),
        "sp_defense": int(input("Defensa especial: ")),
        "speed": int(input("Velocidad: "))
    }
    
    new_pokemon = { 
        "name": name,
        "type": typ,
        "level": level,
        "weight_kg": weight,
        "is_shiny": shiny,
        "held_item": held_item,
        "skills": skills_list,
        "stats": stats
    }
    
    return new_pokemon

def main():
    file_name = "pokemon.json"
    
    existing_pokemons = checkpk(file_name)
    
    new_pokemon = get_pokemon()
    
    existing_pokemons.append(new_pokemon)
    
    save(file_name, existing_pokemons)
    
    print(f"\n¡{new_pokemon['name']} ha sido agregado exitosamente!")


main()
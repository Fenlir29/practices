global_var = 29

def phrase_1():
    local_var = 29
    print("se esta quemando el carro")
    phrase_2()

def phrase_2():
    global global_var
    global_var = global_var + 3 
    print("le echo agua?")

def main():
    phrase_1()
    phrase_2()
    print(f"{global_var}")

print(local_var)
main()

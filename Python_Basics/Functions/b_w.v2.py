def backwards(my_string):
    result = ""
    for i in range(len(my_string)-1,-1,-1):
        result = result + my_string[i]
    return result



def main():
    my_string = "Hello World"
    print(backwards(my_string))

main()
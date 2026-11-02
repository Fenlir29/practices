
def total_list(my_list):
    total = 0
    for number in my_list:
        total += number
    return total

def main():
    my_list = [2,13,75,43,8,29]
    total = total_list(my_list)
    print(total)

main()
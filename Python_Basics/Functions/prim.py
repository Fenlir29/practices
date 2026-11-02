def prime_num(num):          
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


def prim(nums):              
    list_prime = []
    for num in nums:
        if prime_num(num):
            list_prime.append(num)
    return list_prime


def main():
    my_list = [1, 4, 6, 7, 13, 9, 67]
    print(prim(my_list))

main()

# my_list = [1, 4, 6, 7, 13, 9, 67] 

# def prim():
#     list_prime = []
#     for num in my_list:
#         if num > 1:
#             its_prime = True
#             for i in range(2,num):
#                 if num % i == 0:
#                     its_prime = False
#                     break
#             if its_prime:
#                 list_prime.append(num)
#     return list_prime


# def main():
#     list_prime = prim()
#     print(f"{list_prime}")

# main()
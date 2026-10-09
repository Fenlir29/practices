def bubble_sort_backwards(list_to_sort):
    for out_index in range(len(list_to_sort)-1,0,-1):
        for index in range(len(list_to_sort)-1,0,-1):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index - 1]

            if current_element < next_element:
                list_to_sort[index] = next_element
                list_to_sort[index - 1] = current_element

test_list = [10,2,5,6,9,1,8]

bubble_sort_backwards(test_list)
print(test_list)


    




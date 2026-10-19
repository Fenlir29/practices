def bubble_sort(list_to_sort):
  for outer_index in range(0, len(list_to_sort) - 1):
    has_made_changes = False
    for index in range(0, len(list_to_sort) - 1 - outer_index):
      current_element = list_to_sort[index]
      next_element = list_to_sort[index + 1]

      print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')

      if current_element > next_element:
        print('El elemento actual es mayor al siguiente. Intercambiandolos...')
        list_to_sort[index] = next_element
        list_to_sort[index + 1] = current_element
        has_made_changes = True

    if not has_made_changes:
      return

# (O(n^2)) en el peor caso

def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)

# (O(n))

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False
# (O(n))

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])

# (O(1))

def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

# (O(n * m * p))
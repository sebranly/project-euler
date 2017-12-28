# This is required for execution speed
list_known_values = []

def get_number_of_lattice_paths(width_height_tuple):
    if (width_height_tuple[0] == 0 or width_height_tuple[1] == 0):
        if (width_height_tuple[0] == 0):
            return width_height_tuple[1]
        else:
            return width_height_tuple[0]
    if (width_height_tuple[0] == 1 and width_height_tuple[1] == 1):
        return 2
    if (width_height_tuple[0] == 2 and width_height_tuple[1] == 2):
        return 6
    if (width_height_tuple[0] == 1 or width_height_tuple[1] == 1):
        if (width_height_tuple[0] == 1):
            other_size = width_height_tuple[1]
        else:
            other_size = width_height_tuple[0]
        return 2 + other_size - 1
    for element in list_known_values:
        if (element[0][0] == width_height_tuple[0] and element[0][1] == width_height_tuple[1]):
            return element[1]
    if (width_height_tuple[0] == width_height_tuple[1]):
        result = 2 * get_number_of_lattice_paths([width_height_tuple[0] - 1, width_height_tuple[1]])
    else:
        result = get_number_of_lattice_paths([width_height_tuple[0] - 1, width_height_tuple[1]]) \
                 + get_number_of_lattice_paths([width_height_tuple[0], width_height_tuple[1] - 1])
    list_known_values.append([[width_height_tuple[0], width_height_tuple[1]], result])
    return result

for i in range(1, 21):
    if (i == 20):
        print("final result: ")
    print(get_number_of_lattice_paths([i, i]))
      

# I am aware we might find numbers greater than this in the sequence but I want to fix an arbitrary limit
limit_known_values = 1000000
known_values = [-1] * limit_known_values

def length_collatz_sequence(number):
    sequence = [number]
    length = 0
    already_known_length = False
    while (number != 1):
        already_known_length = False
        if (number < limit_known_values and known_values[number] != -1):
            length += known_values[number]
            already_known_length = True
            break
        length += 1
        if (number % 2 == 0):
            number = int(number / 2)
        else:
            number *= 3
            number += 1
        sequence.append(number)
    if (not already_known_length):
        length += 1

    copy_length = length
    for number_sequence in sequence:
        if (number_sequence < limit_known_values and known_values[number_sequence] == -1):
            known_values[number_sequence] = copy_length
        else:
            break
        copy_length -= 1      
    return length

longest_length = 1
associated_starting_number = 1

for i in range(2, 1000000):
    length_sequence = length_collatz_sequence(i)
    if (length_sequence > longest_length):
        longest_length = length_sequence
        associated_starting_number = i
print(associated_starting_number)

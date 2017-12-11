th_prime_number_being_searched = 10001
arbitrary_size = 1000000

prime_numbers = [True] * arbitrary_size
prime_numbers[1] = False
counter_prime_numbers = 0
i = 1
continue_search = True
while (i < arbitrary_size - 1 and continue_search):
    i += 1
    if (prime_numbers[i]):
        counter_prime_numbers += 1
        if (counter_prime_numbers == th_prime_number_being_searched):
            continue_search = False
        else:
            number = 2 * i
            while (number < arbitrary_size):
                prime_numbers[number] = False
                number += i
if (continue_search):
    print("Please increase the arbitrary size or reduce the position of the prime number to be searched for (or do both)")
else:
    print(i)

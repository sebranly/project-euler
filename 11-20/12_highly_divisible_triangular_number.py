def build_prime_numbers_list(limit):
    prime_numbers = [True] * limit
    prime_numbers[1] = False
    i = 1
    while (i < limit - 1):
        i += 1
        if (prime_numbers[i]):
            number = 2 * i
            while (number < limit):
                prime_numbers[number] = False
                number += i
    prime_numbers_list = []
    counter = 0
    for i in range(2, limit):
        if (prime_numbers[i]):
            prime_numbers_list.insert(counter, i)
            counter += 1
    return prime_numbers_list

print("Preparing a long list of prime numbers...")
list_prime = build_prime_numbers_list(1000000)
print("Done preparing the list")
required_number_of_divisors = 501
number = 1
triangular_number = 1
number_of_divisors = 1
while (number_of_divisors < required_number_of_divisors):
    number += 1
    triangular_number += number
    decomposition = []
    decomposed_number = triangular_number
    i = 0
    new_entry = False
    while(decomposed_number != 1):
        if (decomposed_number % list_prime[i] == 0):
            if (new_entry):
                # We increase the pow of the same prime number we got at the previous iteration
                decomposition[len(decomposition) - 1][1] += 1
            else:
                new_entry = True
                # We insert a new decomposition element like [prime_number, 1] with 1 being a pow
                decomposition.insert(len(decomposition), [list_prime[i], 1])
            decomposed_number /= list_prime[i]
        else:
            # When we are done with a prime number because we found all the pows, we go to the next one
            i += 1
            new_entry = False
    number_of_divisors = 1
    # Formula: number_of_divisors = (pow1 + 1) * (pow2 + 1) * ... * (pown + 1) after the prime number decomposition
    for j in range(0, len(decomposition)):
        number_of_divisors *= (decomposition[j][1] + 1)
print(triangular_number)
print(decomposition)
print(number_of_divisors)

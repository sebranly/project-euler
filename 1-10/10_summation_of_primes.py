limit = 2000000

prime_numbers = [True] * limit
prime_numbers[1] = False
i = 1
sum_prime_numbers = 0
while (i < limit - 1):
    i += 1
    if (prime_numbers[i]):
        sum_prime_numbers += i
        number = 2 * i
        while (number < limit):
            prime_numbers[number] = False
            number += i
print(sum_prime_numbers)

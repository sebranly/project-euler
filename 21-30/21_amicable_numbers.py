limit = 10000
sum_divisors = 0
val = [0, 0]
for number in range(2, limit):
    sum_divisor = 0
    for number2 in range(1, int(number / 2) + 1):
        if (number % number2 == 0):
            sum_divisor += number2
    val.append(sum_divisor)

sum_amicable_numbers = 0
for number in range(2, limit):
    if (val[number] < limit and number != val[number] and val[val[number]] == number):
        sum_amicable_numbers += number
print(sum_amicable_numbers)

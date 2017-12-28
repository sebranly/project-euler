def factorial(number, accumulator = 1):
    if (number == 0):
        return accumulator
    return factorial(number - 1, accumulator * number)

result = factorial(100)
sum_digits = 0
for digit in str(result):
    sum_digits += int(digit)
print(sum_digits)
    

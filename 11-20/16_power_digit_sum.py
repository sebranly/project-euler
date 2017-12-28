number = pow(2, 1000)
sum_digits = 0
for digit in str(number):
    sum_digits += int(digit)
print(sum_digits)

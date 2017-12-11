def is_a_palindromic_number(number):
    return str(number) == str(number)[::-1]

maxPalindromicNumber = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if (is_a_palindromic_number(product) and product > maxPalindromicNumber):
            maxPalindromicNumber = product
print(maxPalindromicNumber)

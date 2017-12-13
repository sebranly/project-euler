def important_number():
    return 1000

def calculate_c(a, b):
    return important_number() - (a + b)

a = 1
b = 2
c = calculate_c(a, b)
while ((a * a + b * b) != (c * c)):
    b += 1
    if (a + b >= important_number()):
        a += 1
        b = a + 1
    c = calculate_c(a, b)
    
print(a * b * c)

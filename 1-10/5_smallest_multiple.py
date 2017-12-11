number = 2520
keep_iterating = True
while (keep_iterating):
    if (number % 10000000 == 0):
        print(number)
    evenly_disible = True
    i = 20
    # If we can divide it by 20 then we can divide it by 2, 4, 5, 10
    # By doing so with numbers from 20 to 11, we conclude that numbers from 1 to 10 are useless
    while (i > 10 and evenly_disible):
        if (number % i != 0):
            evenly_disible = False
        else:
            i -= 1
    if (evenly_disible):
        keep_iterating = False
    else:
        number += 2520
print(number)

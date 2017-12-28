limit = 1000
# This is ordered so that we can have the length of "three" by doing list_known_values[3]
# 0 to 19
# For zero we set it to 0 (even though it should be 4) so that we don't have multiple cases to handle
val = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

# No logic was implemented for beyond 1000 on purpose because of the scope of the problem
def get_number_of_letters(number):
    if (number < len(val)):
        return val[number]
    if (number == 20 or number == 30 or number == 80 or number == 90):
        val.append(6)
        return 6
    if (number == 40 or number == 50 or number == 60):
        val.append(5)
        return 5
    if (number == 70):
        val.append(7)
        return 7
    if (number == 100):
        val.append(7)
        # Edge-case: the first time we see it, we add "one"
        return 7 + 3
    if (number == 1000):
        val.append(8)
        # Edge-case: the first time we see it, we add "one"
        return 8 + 3
    if (number < 100):
        result = get_number_of_letters(int(number / 10) * 10) + get_number_of_letters(number % 10)
        val.append(result)
        return result
    # Then we can decompose it as 100 * a + bc 
    a = int(str(number)[0])
    bc = number - 100 * a
    result = get_number_of_letters(a) + get_number_of_letters(100)
    if (bc != 0):
        result += 3 + get_number_of_letters(bc)
    val.append(result)
    return result

counter_letters = 0
for i in range(1, limit + 1):
    counter_letters += get_number_of_letters(i)
print(counter_letters)

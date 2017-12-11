number = 600851475143
counter = 2
if (number > 1):
    while (number != 1):
        if (number % counter == 0):
            number = number / counter
        else:
            counter += 1
    print(counter)
else:
    print("Please use a number stricly greater than 1")
        

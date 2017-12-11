previousTerm = 1
maxTerm = 2
sumEvenTerms = 2
while (maxTerm < 4000000):
    temp = maxTerm
    maxTerm += previousTerm
    previousTerm = temp
    if (maxTerm % 2 == 0):
        sumEvenTerms += maxTerm
print(sumEvenTerms)

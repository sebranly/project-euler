sumRange = 0
sumSquareRange = 0
for i in range(1,101):
    sumSquareRange += i * i
    sumRange += i
print(sumRange * sumRange - sumSquareRange)
    

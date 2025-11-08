numbers = []
for i in range(10000000):
    #to remove 0 and 1
    i = i + 10

    #print(i)
    sum = 0
    for digit in str(i):
        sum += int(digit)**5
    #print(i - sum)
    if sum == i:
        numbers.append(i)
print(numbers)
#see no change beetween 1m and 10m, assuming there no larger number possible
sum = 0
for i in numbers:
    sum += i
print(sum)
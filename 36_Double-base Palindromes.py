sum = 0
for i in range(1, 1000000):
    base_two = str(bin(i))[2:]
    if str(i) == str(i)[::-1]:
        if base_two == base_two[::-1]:
            sum += i
            print(i)
            print(base_two)

print("sum: " + str(sum))
eighty_nine_ended = 0
for i in range(1, 10000000):
    a = i
    while a != 89 and a != 1:
        sum_of_squares = 0
        digits = str(a)
        for digit in digits:
            sum_of_squares += int(digit)**2
        a = sum_of_squares
    if a == 89:
        eighty_nine_ended += 1
print(eighty_nine_ended)
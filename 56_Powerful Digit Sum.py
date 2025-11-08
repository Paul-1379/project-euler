def digital_sum(a, b):
    text = str(a**b)
    sum = 0
    for i in text:
        sum += int(i)
    return sum

max = 0
for a in range(2, 100):
    for b in range(1, 99):
        sum = digital_sum(a, b)
        if(sum > max):
            max = sum
print(max)
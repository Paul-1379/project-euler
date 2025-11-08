def is_lychrel(num):
    for i in range(50):
        num += int(str(num)[::-1])
        if(str(num) == str(num)[::-1]):
            return False
    return True

total = 0
for i in range(10000):
    if(is_lychrel(i)):
        total += 1
print(total)
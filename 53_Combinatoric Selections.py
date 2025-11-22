factorials = []
product = 1
for i in range(101):
    factorials.append(product)
    product *= i + 1

def selection(n, r):
    return factorials[n] / (factorials[r]  * factorials[n - r])

total = 0
for n in range(1, 101):
    for r in range(1, 101):
        if r >= n:
            break

        if selection(n, r) > 1000000:
            total += 1
    print("progress: " + str(n / 100))

print(selection(23, 10))
print(total)

        

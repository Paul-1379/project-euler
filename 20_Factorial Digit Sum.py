number = 1
for i in range(100):
	number *= i + 1
sum = 0
for digit in str(number):
	sum += int(digit)

print(sum)
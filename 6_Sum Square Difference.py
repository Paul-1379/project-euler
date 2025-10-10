sum_squares = 0
sum = 0
for i in range(101):
	sum_squares += i * i
	sum += i

print(sum * sum - sum_squares)
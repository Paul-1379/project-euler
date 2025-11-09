def get_sum_of_proper_divisors(n):
	sum = 0
	for i in range(int(n**(1/2))):
		if n % (i + 1) == 0:
			sum += (i + 1)+(n/(i+1))
	return int(sum - n)

total_sum = 0
for i in range(10000):
	sum_of_proper_divisors = get_sum_of_proper_divisors(i)
	if sum_of_proper_divisors != i and get_sum_of_proper_divisors(sum_of_proper_divisors) == i:
		total_sum += i
print(total_sum)
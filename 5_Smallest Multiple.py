found = False
n = 20
while not found:
	all_divisors = True
	for i in range(11, 20):
		if n % i != 0:
			all_divisors = False
			break

	if all_divisors:
		print(n)
		found = True
	n += 20
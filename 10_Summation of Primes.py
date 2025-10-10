primes = [2]
largest_prime = 0
sum = 0
i = 3
while largest_prime < 2000000:
	for prime in primes:
		is_prime = True
		if i % prime == 0:
			is_prime = False
			break
	if i > largest_prime:
		largest_prime = i
		if largest_prime > 500000:
			print(largest_prime)
	if is_prime:
		primes.append(i)
		sum += i
	i += 2

sum
primes = [2]
i = 3
while len(primes) < 10001:
	for prime in primes:
		is_prime = True
		if i % prime == 0:
			is_prime = False
			break
	if is_prime:
		primes.append(i)

	i += 2
	print(len(primes))

print(primes[-1])
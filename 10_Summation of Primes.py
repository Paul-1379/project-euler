def eratostene_sum(n):
	sum = 0

	primes = [True] * n
	i = 2
	while i < n:
		j = 2
		while i * j < n + 1:
			primes[i * j - 1] = False
			j += 1
		sum += i
		i += 1
		while not primes[i - 1]:
			i += 1
			if i > n - 1:
				break
	
	print(sum)

eratostene_sum(2000000)
print("ended")
def eratostene(n):
	found_primes = []
	primes = [True] * n
	i = 2
	while i < n:
		j = 2
		while i * j < n + 1:
			primes[i * j - 1] = False
			j += 1
		found_primes.append(i)
		i += 1
		while not primes[i - 1]:
			i += 1
			if i > n - 1:
				return found_primes

def is_circular_prime(prime, all_primes):
    text = str(prime)
    start = True
    while text != str(prime) or start:
        start = False
        #one rotation
        first_digit = text[0]
        text = text[1:]
        text += first_digit

        if not all_primes.__contains__(int(text)):
            return False
    return True

circular_primes_number = 0
primes = eratostene(1000000)
for prime in primes:
    print(primes.index(prime) / len(primes))
    if is_circular_prime(prime, primes):
        circular_primes_number += 1

print(circular_primes_number)
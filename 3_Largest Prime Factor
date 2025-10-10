big_number = 600851475143

#1st try, too slow

# primes = [2]

# #calculate primes up to big_number
# for i in range(big_number):
# 	for prime in primes:
# 		if (i + 1) % prime == 0:
# 			break
# 	primes.append(i + 1)
# 	print(i / big_number * 100)

# #check which primes are factors of big_number
# biggest_prime = 0
# for prime in primes:
# 	if big_number % prime == 0:
# 		if prime > biggest_prime:
# 			biggest_prime = prime
			
# print("finished: " + str(biggest_prime))

#2nd try, still too slow
# divisors = []
# for i in range(round(big_number / 2)):
# 	if big_number % (i + 1) == 0:
# 		divisors.append((i + 1))
# 		print(i / big_number * 100)


def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

for i in range(round(big_number / 2)):
	if big_number % (i + 1) == 0:
		if is_prime(int(big_number / (i + 1))):
			print("found prime factor: " + str(big_number / (i + 1)))
			break
		print(i / big_number * 100)

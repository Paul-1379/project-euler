def eratostene(n):
    prime_numbers = []
    primes = [True] * n
    i = 2
    while i < n:
        j = 2
        while i * j < n + 1:
            primes[i * j - 1] = False
            j += 1

        i += 1
        prime_numbers.append(i)
        while not primes[i - 1]:
            i += 1
            if i > n - 1:
                break
	
    return prime_numbers

primes = eratostene(7072)
print("primes found")

found_numbers = []
for a in primes:
    if a**2 > 50000000:
        break
    print()
    for b in primes:
        if a**2+b**3 > 50000000:
            break
        for c in primes:
            result = a**2+b**3+b**4
            if result < 50000000:
                if not found_numbers.__contains__(result):
                    found_numbers.append(result)
                #else:
                    #print("contains")
            else:
                print("brek")
                break

print(len(found_numbers))
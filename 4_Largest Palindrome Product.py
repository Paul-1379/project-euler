
def found_biggest_palindrome():
	biggest = 0

	for i in range(1000):
		for j in range(1000):
			product = (1000 - (i + 1)) * (1000 - (j + 1))
			if str(product) == str(product)[::-1]:
				#print("i: " + str(1000 - (i + 1)) + " j: " + str(1000 - (j + 1)) + " product: " + str(product))
				if(product > biggest):
					biggest = product
	return biggest

print(found_biggest_palindrome())
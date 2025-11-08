def get_divisors_number(n):
	divisor_number = 0
	for i in range(int(n**(1/2))):
		if n % (i + 1) == 0:
			divisor_number += 2
	return divisor_number
# print(get_divisors_number(28))
current_triangular_adding = 1
current_triangular_number = 1
max_div_number = 0
while True:
	div_number = get_divisors_number(current_triangular_number)
	if div_number > max_div_number:
		max_div_number = div_number
		print(div_number)
		print(current_triangular_number)
	current_triangular_adding += 1
	current_triangular_number += current_triangular_adding
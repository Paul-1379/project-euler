def get_divisors_number(n):
	divisor_number = 1
	done = []
	for i in range(int(n/2)):
		if(done.__contains__(i + 1)):
			continue
		if n % (i + 1) == 0:
			done.append(int(n / divisor_number))
			divisor_number += 2
	return divisor_number

current_triangular_adding = 1
current_triangular_number = 1
max_div_number = 0
while True:
	div_number = get_divisors_number(current_triangular_number)
	if div_number > max_div_number:
		max_div_number = div_number
		print(div_number)
	current_triangular_adding += 1
	current_triangular_number += current_triangular_adding
know_number_lenght = [0] * 1000000 #full of 0

def calculate_chain_lenght(n):
	if n > len(know_number_lenght) - 1 or know_number_lenght[n] == 0:
		steps = 1
		if n % 2 == 0:
			n = int(n/2)
		else:
			n = 3*n + 1
		if n != 1:
			steps += calculate_chain_lenght(n)

		if n < len(know_number_lenght):
			know_number_lenght[n] = steps
	else:
		steps = know_number_lenght[n]
	return steps

longest_chain = 0
longest_chain_start = 0
for i in range(1000000 - 1):
	lenght = calculate_chain_lenght(i + 1)
	if(lenght > longest_chain):
		longest_chain = lenght
		longest_chain_start = i + 1

print(longest_chain_start)
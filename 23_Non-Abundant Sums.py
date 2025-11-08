#1st fidn all abundant numbers under 28123
def get_divisors_sum(n):
	divisors_sum = 0
	for i in range(int(n/2)):
		if n % (i + 1) == 0:
			divisors_sum += i+1
		
	return divisors_sum

abundant_numbers = []
for i in range(28123):
	if get_divisors_sum(i) > i:
		abundant_numbers.append(i)
		#print(i / 28123)

#2nd find numbers (under 28123) who can be written as the sum of 2 abundant numbers
possible_sums = []
total = len(abundant_numbers)
index = 0
while len(abundant_numbers) > 0:
	index += 1
	for ab_num2 in abundant_numbers:

		sum = abundant_numbers[0]+ab_num2
		if sum <= 28123:
			continue
		if not possible_sums.__contains__(sum):
			possible_sums.append(sum)
	if index % 10 == 0:
		print(index / total)
	abundant_numbers.pop(0)
#3rd cumpute the sum
total_sum = 0
for i in possible_sums:
	total_sum += i

print(total_sum)
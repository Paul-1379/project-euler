a = 1
b = 2
index = 1
while len(str(a)) < 3:
	index += 1
	a, b = b, a + b

print(index + 1)
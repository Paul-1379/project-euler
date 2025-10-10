a = 0
for i in range(819000):
	b = i * i
	if b%2 == 1:
		a += b

print(a)
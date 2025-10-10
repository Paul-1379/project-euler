for i in range(1000):
	for j in range(i, 1000):
		c = (i**2 + j**2)**0.5
		if i + j + c == 1000:
			print("i: ", i, " j: ", j, " c: ", c)
			break
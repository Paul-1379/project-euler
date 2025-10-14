size = 20
known_pos = [[0 for x in range(size + 1)] for y in range(size + 1)] 
def count_pos(x, y):
	if known_pos[x][y] != 0:
		return known_pos[x][y]
	else:
		pos = 0
		if x == size and y == size:
			known_pos[x][y] = 1
			return 1
		
		if x < size:
			pos += count_pos(x + 1, y)
		if y < size:
			pos += count_pos(x, y + 1)

		known_pos[x][y] = pos
		return pos
	
pos = count_pos(0, 0)
print(pos)
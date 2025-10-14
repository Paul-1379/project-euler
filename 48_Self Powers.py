sum = 0
for i in range(999):
	sum += (i+1)**(i+1)

sum_text = str(sum)
text = ""
for i in range(10):
	text += sum_text[len(sum_text) - i - 1]

print(text[::-1])

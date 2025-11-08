terms = []
for a in range(2, 101):
    print(a/100)
    for b in range(2, 101):
        num = a**b
        if not terms.__contains__(num):
            terms.append(num)
print(len(terms))
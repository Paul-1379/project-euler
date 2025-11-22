def is_valid(a):
    base_digits = sorted(str(a))
    two_digits = sorted(str(a * 2))
    tree_digits = sorted(str(a * 3))
    four_digits = sorted(str(a * 4))
    five_digits = sorted(str(a * 5))
    six_digits = sorted(str(a * 6))
    return base_digits == two_digits == tree_digits == four_digits == five_digits

for i in range(1, 1000000):
    if is_valid(i):
        print(i)
        break

print("not found")
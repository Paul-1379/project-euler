def get_digits_fact_sum(num):
    sum = 0
    text = str(num)
    for digit in text:
        sum += factorial(int(digit))
    return sum

def factorial(num):
    product = 1
    for i in range(num):
        product *= (i+1)
    return product

for i in range(10000000):
    sum = get_digits_fact_sum(i)
    if i == sum:
        print(i)
#145+40585=40730
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

def get_chain_lenght(num):
    seen_numbers = [num]
    num = get_digits_fact_sum(num)
    lenght = 1
    while not seen_numbers.__contains__(num):
        lenght += 1
        seen_numbers.append(num)
        num = get_digits_fact_sum(num)
    return lenght

chains_number = 0
for i in range(1000000 - 1):
    print(i/1000000)
    if get_chain_lenght(i+1) == 60:
        chains_number += 1
print(chains_number)
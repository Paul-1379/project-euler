coins = [200, 100, 50, 20, 10, 5, 2, 1]
factors = [0] * 8
max_factors = [0]*8
for i in range(8):
    max_factors[i] = int(200/coins[i])

print(max_factors)
def compute_weighted_sum():
    sum = 0
    for coin in coins:
        sum += coin * factors[coins.index(coin)]

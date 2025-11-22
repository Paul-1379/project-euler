def pentagon(n):
    return int((n*(3*n-1))/2)

pentagonals = []
for i in range(1, 10001):
    pentagonals.append(pentagon(i))

smallest = float('inf')
for j in range(1, 1000):
    print(j / 1000)
    for k in range(1, 1000):
        diff = abs(pentagonals[j - 1] - pentagonals[k - 1])
        if pentagonals.__contains__(pentagonals[j - 1] + pentagonals[k - 1]) and pentagonals.__contains__(diff):
            if diff < smallest:
                print(j)
                print(k)
                smallest = diff
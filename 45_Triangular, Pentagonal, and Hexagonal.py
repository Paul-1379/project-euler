def pentagon(n):
    return int((n*(3*n-1))/2)
def triangle(n):
    return int((n*(n+1))/2)
def hexagonal(n):
    return int(n*(2*n-1))

penta = []
hexa = []
for i in range(1, 100000):
    penta.append(pentagon(i))
    hexa.append(hexagonal(i))
    n_triangle = triangle(i)
    if penta.__contains__(n_triangle) and hexa.__contains__(n_triangle):
        print(n_triangle)
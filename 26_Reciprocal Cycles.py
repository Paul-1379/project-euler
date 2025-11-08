def get_cycle_lenght(divider):
    lenght = 0
    divided_seen = []
    divided = 1
    while not divided_seen.__contains__(divided):
        divided_seen.append(divided)
        if divider < divided:
            divided = divided % divider
        
        divided *= 10

        lenght += 1
        if divided == 0:
            return lenght - 1
    return lenght - 1

max = 0
for i in range(2, 1000):
    lenght = get_cycle_lenght(i)
    print("i: " + str(i) + " len: " + str(lenght))
    
    if lenght>max:
        max = lenght
print(max)
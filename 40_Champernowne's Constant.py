index = 0
text = ""
target_indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]
product = 1
for i in range(1, 1000000):
    if index >= target_indexes[0]:
        print("text: " + text + " size: " + str(index))
        print(index - target_indexes[0])
        product *= int(text[-(index - target_indexes[0] + 1)])
        target_indexes.pop(0)
        if len(target_indexes) == 0:
            print("finished")
            break
    text = str(i)
    index += len(str(i))

print(product)
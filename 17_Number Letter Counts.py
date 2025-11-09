numbers = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen").split()
numbers_ten = ("twenty thirty forty fifty sixty seventy eighty ninety").split()

def two_digits(a):
    b = numbers_ten[int(str(a)[0]) - 2]
    if str(a)[1] != "0":
        b += " " + numbers[int(str(a)[1])]
    return b
def get_text_for(a):
    text = ""
    if a < 20:
        text = numbers[a]
    elif a < 100:
        text = two_digits(a)
    elif a < 1000:
        text = numbers[int(str(a)[0])] + " hundred"
        if str(a)[1:] == "00":
            return text
        if int(str(a)[1:]) < 20:
            text += " and " + numbers[int(str(a)[1:])]
        else:
            text += " and " + two_digits(int(str(a)[1:]))
    return text
total = ""
for a in range(1, 1000):
    text = get_text_for(a)
    total += text.replace(" ", "")
    print(text)

total += "onethousand"
print(len(total))
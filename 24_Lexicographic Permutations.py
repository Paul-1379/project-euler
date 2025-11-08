permutations = []
digits = ["1", "2"]

def get_all_permutations(my_digits):
    if len(my_digits) == 1:
        return my_digits[0]
    
    perms = []
    for i in range(len(my_digits)):
        #current_perm = [my_digits[i]]
        new_digits = my_digits.copy()
        new_digits.pop(i)
        #print("call for" + str(new_digits))
        #current_perm.append(get_all_permutations(new_digits))
        perms.append(get_all_permutations(new_digits))
    return perms

print(get_all_permutations(digits))
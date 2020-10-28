word = input()

index = 0
alpha_number = 0
alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

while index != len(word):
    if word[index:index+2] in alpha:
        alpha_number += 1
        index += 2
    elif word[index:index+3] == 'dz=':
        alpha_number += 1
        index += 3
    else:
        alpha_number += 1
        index += 1

print(alpha_number)

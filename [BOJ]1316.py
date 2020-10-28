n = int(input())
word_array = [0] * n

for i in range(n):
    word_array[i] = input()

group_word = 0

for word in word_array:
    index = 0
    temp_array = []
    is_groupword = True

    while index != len(word):
        if word[index] not in temp_array:
            temp_array.append(word[index])
            index += 1
        elif word[index] == temp_array[len(temp_array)-1]:
            index += 1
        else:
            is_groupword = False
            index += 1

    if is_groupword:
        group_word += 1

print(group_word)

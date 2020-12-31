import operator

def solution(encrypted_text, key, rotation):
    temp_key = list(key)
    temp_key = list(map(ord, temp_key))
    temp_key = [x - 96 for x in temp_key]
    
    temp_text = list(encrypted_text)
    temp_text = list(map(ord, temp_text))

    cor_rotation = rotation % len(temp_text)
    temp_ans = temp_text[cor_rotation:] + temp_text[:cor_rotation]

    temp_ans = list(map(operator.sub, temp_ans, temp_key))
    
    for i in range(len(temp_ans)):
        if temp_ans[i] < 97:
            temp_ans[i] += 26
    
    temp_ans_2 = list(map(chr, temp_ans))
    
    answer = ''.join(temp_ans_2)
    return answer

print(solution('qyyigoptvfb', 'abcdefghijk', 3))

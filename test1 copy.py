def solution(N, number):
    answer_list = [[],[],[],[],[],[],[],[]]

    if N == number:
        return 1

    for i in range(8):
        answer_list[i].append(int(str(N)*(i+1)))

    for i in range(2,9):
        for j in range(len(answer_list[i-2])):
            answer_list[i-1].append(answer_list[i-2][j] * N)
            answer_list[i-1].append(answer_list[i-2][j] + N)
            answer_list[i-1].append(N - answer_list[i-2][j])
            answer_list[i-1].append(answer_list[i-2][j] - N)
            if answer_list[i-2][j] != 0:
                answer_list[i-1].append(answer_list[i-2][j] // N)
                answer_list[i-1].append(N // answer_list[i-2][j])
            answer_list[i-1].append(answer_list[i-2][j])
            if i > 2 and i != 8:
                answer_list[i].append(answer_list[i-2][j]+ 1)
                answer_list[i].append(answer_list[i-2][j]- 1)
                answer_list[i].append(answer_list[i-2][j] + answer_list[i-3][0])

        if number in answer_list[i-1]:
            return i
        else:
            answer_list[i-1] = list(set(answer_list[i-1]))
        if i == 5:
            print(answer_list[i-1])
    return -1

# print(1,1121,solution(1,1121),7)
print(5,1010,solution(5,1010),7)
# print(6,65,solution(6,65),4)
# print(7,7776,solution(7,7776),6)
# print(2,22223,solution(2,22223),7)
# print(4,17,solution(4,17),4)
# print(5,24,solution(5,24),4)
# print(5,26,solution(5,26),4)
print('------------------------------')



# print(f'5/12 : {solution(5,12)} 4')
# print(2,11,solution(2,11),3)
# print(5,5,solution(5,5),1)
# print(5,10,solution(5,10),2)
# print(5,31168,solution(5,31168),-1)
# print(3,4,solution(3,4),3)
# print(5,5555,solution(5,5555),4)
# print(5,5550,solution(5,5550),5)
# print(5,20,solution(5,20),3)
# print(5,30,solution(5,30),3)
# print(5,2,solution(5,2),3)
# print(5,4,solution(5,4),3)
# print(1,1,solution(1,1),1)
# print(1,11,solution(1,11),2)
# print(1,111,solution(1,111),3)
# print(1,1111,solution(1,1111),4)
# print(1,11111,solution(1,11111),5)
# print(7,7784,solution(7,7784),5)
# print(2,22222,solution(2,22222),5)
# print(2,22224,solution(2,22224),6)
# print(2,11111,solution(2,11111),6)
# print(2,11,solution(2,11),3)
# print(2,111,solution(2,111),4)
# print(2,1111,solution(2,1111),5)
# print(9,36,solution(9,36),4)
# print(9,37,solution(9,37),6)
# print(9,72,solution(9,72),3)
# print(3,18,solution(3,18),3)
# print(2,1,solution(2,1),2)

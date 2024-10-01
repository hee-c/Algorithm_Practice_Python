def solution(string):
  minimum = 1001

  for slice_num in range(1, len(string) + 1):

    compare_string = ''
    count = 1
    answer = ''

    for current_index in range(0, len(string), slice_num):
      current_string = string[current_index : current_index + slice_num]

      if (compare_string == ''):
        compare_string = current_string
      else:
        if (current_string == compare_string):
          count += 1
        else:
          if (count == 1):
            answer = answer + compare_string
          else:
            answer = answer + f'{count}{compare_string}'
          compare_string = current_string
          count = 1

      if (current_index + slice_num >= len(string)):
        if (count == 1):
            answer = answer + compare_string
        else:
          answer = answer + f'{count}{compare_string}'

        if (len(answer) < minimum):
          minimum = len(answer)

  return minimum

s = input()

print(solution(s))

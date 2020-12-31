from functools import reduce
def solution(n, times):
    times.sort()

    # minimum = (n * times[0]) // len(times)
    # maximum = (n * times[len(times)-1]) // len(times)
    minimum = 0
    maximum = 999999
    process_time = list(range(minimum, maximum + 1))

    start = 1
    end = len(process_time) - 1

    def binary_search(process_time, n, start, end):
        while start <= end:
            mid = (start + end) // 2
            capability = reduce(lambda x, y: x + y, list(map(lambda x: process_time[mid] // x, list(filter(lambda x: x <= process_time[mid], times)))), 0)

            if capability == n:
                return mid
            elif capability > n:
                end = mid - 1
            else:
                start = mid + 1
        return None

    return binary_search(process_time, n, start, end)

print(solution(2, [2,2]))
# print(solution(6, [7,10]))
# print(solution(5, [1,2,3,4,5,6,7,8,9,10]))

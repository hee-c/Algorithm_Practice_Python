n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += a[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= a[start]
print(count)



# for i in range(len(a)):
#     total = 0
#     for j in range(i, len(a)):
#         total += a[j]
#         if total == m:
#             cases += 1
#             break
#         if total > m:
#             break

# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if sum(a[i:j+1]) == m:
#             cases += 1
#             break
#         elif sum(a[i:j+1]) > m:
#             break

s = int(input())
if (s%4==0 and not s%100==0) or (s%4==0 and s%400==0):
    print('1')
else: print('0')
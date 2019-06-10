import math
n = int(input())
a = input().split()
a = [int(m) for m in a]
#a.sort()

x = []
#nが偶数の時
if n % 2 == 0:
    for i in range(1, n + 1):
        if i == n//2 + 1:
            x.append([a[i - 1], 2 * i - 2])
        elif i < n//2 + 1:
            x.append([a[i - 1], 2 * i - 1])
        elif i > n//2 + 1:
            x.append([a[i - 1], 2 * (2 * (n//2 + 1) - i) - 2])
else:
    for i in range(1, n + 1):
        if i == math.ceil(n / 2):
            x.append([a[i - 1], 2 * i - 1])
        elif i < math.ceil(n / 2):
            x.append([a[i - 1], 2 * i - 1])
        elif i > math.ceil(n / 2):
            x.append([a[i - 1], 2 * (2 * (math.ceil(n / 2)) - i)])

y = 0
t = n * (n + 1) // 4 + 1
for i in range(n):
    y += x[i][1]
    if y < t:
        pass
    else:
        print(x[i][0])
        exit()

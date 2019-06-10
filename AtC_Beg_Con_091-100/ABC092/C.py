n = int(input())
a = [int(x) for x in input().split()]
b = []

for i in range(n + 1):
    if i == 0:
        b.append(abs(a[i]))
    elif i == n:
        b.append(abs(a[i - 1]))
    else:
        b.append(abs(a[i] - a[i - 1]))

sd = sum(b)

for j in range(n):
    if j == 0:
        print(sd - b[j] - b[j + 1] + abs(a[j + 1]))
    elif j == n - 1:
        print(sd - b[j] - b[j + 1] + abs(a[j - 1]))
    else:
        print(sd - b[j] - b[j + 1] + abs(a[j + 1] - a[j - 1]))

import math
n, m, k = map(int, input().split())
a = [int(m) for m in input().split()]
b = [int(m) for m in input().split()]
"""x = 0
y = 0
for i in range(n):
    x += math.log10(a[i] * (k ** (n - i - 1)))
for i in range(m):
    y += math.log10(b[i] * (k ** (m - i - 1)))

if x > y:
    print("Y")
elif x < y:
    print("X")
else:
    print("Same")"""
if n > m:
    print("Y")
    exit()
elif n < m:
    print("X")
    exit()
else:
    for i in range(n):
        if a[i] > b[i]:
            print("Y")
            exit()
        elif a[i] < b[i]:
            print("X")
            exit()

print("Same")
a, b, k = map(int, input().split())

for p in range(k):
    if p % 2 == 0:
        if a % 2 != 0:
            a = a - 1
        b = int(b + a/2)
        a = int(a/2)
    else:
        if b % 2 != 0:
            b = b - 1
        a = int(a + b/2)
        b = int(b/2)

print(a, b)
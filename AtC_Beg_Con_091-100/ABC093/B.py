a, b, k = map(int, input().split())
c = b - a + 1
if c % 2 == 0:
    if k >= c / 2:
        for i in range(a, b + 1):
            print(i)
    else:
        for j in range(a, a + k):
            print(j)
        for k in range(b - k + 1, b + 1):
            print(k)
if c % 2 != 0:
    if k >= (c + 1) / 2:
        for i in range(a, b + 1):
            print(i)
    else:
        for j in range(a, a + k):
            print(j)
        for k in range(b - k + 1, b + 1):
            print(k)


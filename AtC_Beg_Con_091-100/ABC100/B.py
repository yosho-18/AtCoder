d, n = map(int, input().split())
if d == 0:
    if n < 100:
        print(n)
    else:
        print(101)
elif d == 1:
    if n < 100:
        print(100 * n)
    else:
        print(10100)
else:
    if n < 100:
        print(10000 * n)
    else:
        print(1010000)



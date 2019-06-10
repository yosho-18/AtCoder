n, a, b = map(int, input().split())
if a > b:
    print(0)
elif n == 1:
    if a == b:
        print(1)
    else:
        print(0)
else:
    print((n - 2) * (b - a) + 1)
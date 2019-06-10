x, y = map(int, input().split())

if x < y:
    if abs(x - y) > abs(-x - y):
        print(abs(-x - y) + 1)
    else:
        print(abs(x - y))
else:
    print(min(abs(-x - y) + 1, abs(x - y) + 2))
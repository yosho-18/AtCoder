a, b, c = map(int, input().split())
if c > a + b + 1:
    print(a + b + 1 + b)
else:
    print(c + b)
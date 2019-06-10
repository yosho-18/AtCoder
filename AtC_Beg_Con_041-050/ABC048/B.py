a, b, x = map(int, input().split())
s = b // x
t = a // x
if a % x == 0:
    print(s - t + 1)
else:
    print(s - t)
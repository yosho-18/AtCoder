t, a, b, c, d = map(int, input().split())
if a + c <= t:
    print(b + d)
elif c <= t:
    print(d)
elif a <= t:
    print(b)
else:
    print(0)
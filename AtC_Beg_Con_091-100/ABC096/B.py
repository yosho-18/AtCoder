a, b, c = map(int, input().split())
k = int(input())

t = max(a, b, c)

u = t * (2 ** k)

if t == a:
    print(u + b + c)
elif t == b:
    print(u + a + c)
elif t == c:
    print(u + a + b)
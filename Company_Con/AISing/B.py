n = int(input())
a, b = map(int, input().split())
p = [int(m) for m in input().split()]
q = 0
r = 0
s = 0
for i in range(n):
    if p[i] <= a:
        q += 1
    elif p[i] <= b:
        r += 1
    else:
        s += 1
print(min(q, r, s))
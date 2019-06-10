n, x = map(int, input().split())
n = int(n)
x = int(x)
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
m = [int(k) for k in d]

t = sum(m)
t2 = len(m)
m.sort()

u = int((x - t) / m[0])

print(t2 + u)

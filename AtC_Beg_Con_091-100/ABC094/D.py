n = int(input())
a = [int(x) for x in input().split()]

t = max(a)
b = []

for i in range(n):
  if t != a[i]:
    u = abs(t / 2 - a[i])
    b.append(u)
  else:
    b.append(t)

v = a[b.index(min(b))]
print(t, v)

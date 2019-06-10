x, y, z, k = map(int, input().split())
a = [int(m) for m in input().split()]
b = [int(m) for m in input().split()]
c = [int(m) for m in input().split()]
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
s = []
for i in range(x):
    for j in range(y):
        s.append(a[i] + b[j])

s.sort(reverse=True)
s1 = []
for i in range(min(x * y, k)):
    s1.append(s[i])

t = []
for i in range(min(x * y, k)):
    for j in range(z):
        t.append(s1[i] + c[j])

t.sort(reverse=True)

for i in range(k):
    print(t[i])
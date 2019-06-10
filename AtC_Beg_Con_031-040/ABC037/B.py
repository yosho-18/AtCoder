n, q = map(int, input().split())
c = []
for i in range(q):#h:高さ
    c.append([int(m) for m in input().split()])

a = [0]*n
for i in range(q):
    for j in range(c[i][0] - 1, c[i][1]):
        a[j] = c[i][2]

for i in range(n):
    print(a[i])
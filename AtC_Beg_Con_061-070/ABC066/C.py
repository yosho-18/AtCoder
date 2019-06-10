n = int(input())
a = input().split()
a = [int(m) for m in a]
rea = []
for i in range(n):
    rea.append([i, a[i]])

rea.sort(reverse=True)
b = []
c = []
for i in range(n):
    if i % 2 == 0:
        b.append([rea[i][0], rea[i][1]])
    else:
        c.append([rea[i][0], rea[i][1]])

c.sort()

nb = []
nc = []
for i in range(len(b)):
    nb.append(b[i][1])
for i in range(len(c)):
    nc.append(c[i][1])
nd = nb + nc
for i in range(n):
    print(nd[i], end = ' ')
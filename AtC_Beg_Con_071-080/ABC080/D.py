n, c = map(int, input().split())
r = []
for i in range(n):#h:高さ
    r.append([int(m) for m in input().split()])

r.sort(key=lambda x:(x[0], x[1],x[2]))

xli = []
p = 0
for i in range(n):
    if i == 0:
        xli.append(r[i])
    else:
        xli.sort(key=lambda x: (x[1]), reverse=True)
        for jnum, j in enumerate(xli, 0):
            if (j[1] < r[i][0]) or (j[1] <= r[i][0] and j[2] == r[i][2]):
                p = 1
                xli[jnum] = r[i]
                break
        if p == 0:
            xli.append(r[i])
        p = 0

print(len(xli))

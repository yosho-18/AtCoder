n, m = map(int, input().split())
c = []
for i in range(m):#h:高さ
    c.append([int(m) for m in input().split()])
c.sort(key=lambda x:(x[0], x[1]))
root = []
for i in range(n):
    root.append([])
for i in range(m):
    root[c[i][0] - 1].append(c[i][1])
root1 = root[0]
for v in root1:
    if n in root[v - 1]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
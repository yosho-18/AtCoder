n, m = map(int, input().split())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])
for i in range(n):
    s[i].append(s[i][0] + s[i][1] + s[i][2])
    s[i].append(s[i][0] + s[i][1] - s[i][2])
    s[i].append(s[i][0] - s[i][1] + s[i][2])
    s[i].append(-s[i][0] + s[i][1] + s[i][2])
    s[i].append(s[i][0] - s[i][1] - s[i][2])
    s[i].append(-s[i][0] - s[i][1] + s[i][2])
    s[i].append(-s[i][0] + s[i][1] - s[i][2])
    s[i].append(-s[i][0] - s[i][1] - s[i][2])
maxtotal = 0
for i in range(8):
    s.sort(key=lambda x:(x[i + 3]), reverse=True)
    total = 0
    for j in range(m):
        total += s[j][i + 3]
    if maxtotal < total:
        maxtotal = total
print(maxtotal)

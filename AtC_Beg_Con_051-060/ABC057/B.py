n, m = map(int, input().split())
ab = []
for i in range(n):#h:高さ
    ab.append([int(m) for m in input().split()])
cd = []
for i in range(m):#h:高さ
    cd.append([int(m) for m in input().split()])
dis = [float("inf")]*n
dn = [-1]*n
for i in range(n):
    for j in range(m):
        t = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if t < dis[i]:
            dis[i] = t
            dn[i] = j
    print(dn[i] + 1)

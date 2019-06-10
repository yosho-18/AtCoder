import collections
import itertools
#横にn個入力
n, c = map(int, input().split())
#行列
d = []
for i in range(c):#h:高さ
    d.append([int(m) for m in input().split()])
#行列
e = []
for i in range(n):#h:高さ
    e.append([int(m) for m in input().split()])

li0 = []
li1 = []
li2 = []
for i in range(n):
    for j in range(n):
        if (i + j + 2) % 3 == 0:
            li0.append(e[i][j])
        elif (i + j + 2) % 3 == 1:
            li1.append(e[i][j])
        elif (i + j + 2) % 3 == 2:
            li2.append(e[i][j])

c0 = collections.Counter(li0)
c1 = collections.Counter(li1)
c2 = collections.Counter(li2)

cost0 = {}
cost1 = {}
cost2 = {}
dost0 = []
dost1 = []
dost2 = []
k0 = 0
k1 = 0
k2 = 0
for i in range(c):
    for v0 in c0:
        k0 += d[v0 - 1][i] * c0[v0]
    cost0[i + 1] = k0
    dost0.append([k0, i + 1])
    k0 = 0
    for v1 in c1:
        k1 += d[v1 - 1][i] * c1[v1]
    cost1[i + 1] = k1
    dost1.append([k1, i + 1])
    k1 = 0
    for v2 in c2:
        k2 += d[v2 - 1][i] * c2[v2]
    cost2[i + 1] = k2
    dost2.append([k2, i + 1])
    k2 = 0

dost0.sort()
dost1.sort()
dost2.sort()
w0 = [dost0[0][1], dost0[1][1], dost0[2][1]]
w1 = [dost1[0][1], dost1[1][1], dost1[2][1]]
w2 = [dost2[0][1], dost2[1][1], dost2[2][1]]

ansli = []
for x0 in itertools.permutations(w0, 1):
    for x1 in itertools.permutations(w1, 1):
        for x2 in itertools.permutations(w2, 1):
            if x0[0] != x1[0] and x1[0] != x2[0] and x2[0] != x0[0]:
                ansli.append(cost0[x0[0]] + cost1[x1[0]] + cost2[x2[0]])

print(min(ansli))


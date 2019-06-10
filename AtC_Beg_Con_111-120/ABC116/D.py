#import collections
n, k = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])
c.sort(key=lambda x:(x[0], x[1]))
f = sorted(c, key=lambda x:(x[1], x[0]), reverse=True)
donyoku = 0
donset = set()
for i in range(k):
    donyoku += f[i][1]
    donset.add(f[i][0])
donyoku += len(donset)**2

t = []
d = []
for i in range(n):#h:高さ
    pi, qi = c[i][0], c[i][1]
    t.append(pi)
    d.append(qi)
spe = len(set(t))
stili = []
real = 0
reaset = set()
ws = set()
i = 0
p = [0]*n
while True:
    if f[i][0] not in ws:
        real += f[i][1]
        ws.add(f[i][0])
        p[i] = 1
        i += 1
    if i == len(donset):
        break
kosu = len(donset)
yy = real
u = 0
for i in range(len(donset) + 1, k + 1):
    while True:
        if f[i][0] not in ws:
            real += f[i][1]
            ws.add(f[i][0])
            kosu += 1
            break
        else:
            i += 1
        if i == n:
            u = 1
            break
    if u == 1:
        break
    q = 0
    while True:
        if q < n:
            if p[q] == 0:
                real += f[q][1]
                kosu += 1
                if kosu == k:
                    break
        else:
            break
        q += 1
    real += len(ws) ** 2
    stili.append(real)
    real = yy


if stili != []:
    rr = min(stili)
    print(min(donyoku,rr))
else:
    print(donyoku)
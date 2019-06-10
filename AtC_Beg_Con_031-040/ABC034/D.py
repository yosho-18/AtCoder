n, k = map(int, input().split())
w = []
p = []
for i in range(n):#h:高さ
    pi, qi = map(int, input().split())
    w.append(pi)
    p.append(qi)

tmpdens = 0
dens = 0
weight = 0
flagnum = 0
NaCl = 0
flagli = [0]*n

for i in range(k):
    for j in range(n):
        if flagli[j] == 0:
            tmpdens = (NaCl + p[j] * 0.01 * w[j]) / (weight + w[j])
            if tmpdens > dens:
                flagnum = j
                dens = tmpdens
    flagli[flagnum] = 1
    NaCl += p[flagnum] * 0.01 * w[flagnum]
    weight += w[flagnum]
    dens = 0

dens = NaCl / weight
print(dens * 100)
n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
a = [int(m) for m in d]#int型に直す
aa = sorted(a)
bdic = {}
zaatsucnt = 0
for i in range(n):
    if i == 0:
        bdic[aa[i]] = zaatsucnt
    else:
        if aa[i - 1] != aa[i]:
            zaatsucnt += 1
        bdic[aa[i]] = zaatsucnt

for i in range(n):
    print(bdic[a[i]])
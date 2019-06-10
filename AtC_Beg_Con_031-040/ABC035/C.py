n, q = map(int, input().split())
l = []
r = []
for i in range(q):#h:高さ
    pi, qi = map(int, input().split())
    l.append(pi)
    r.append(qi)

oseroli = [0]*(n + 2)
for i in range(q):
    oseroli[l[i]] += 1
    oseroli[r[i] + 1] -= 1

for i in range(1, n + 1):
    oseroli[i] += oseroli[i - 1]

for i in range(1, n + 1):
    if oseroli[i] % 2 == 0:
        print(0, end="")
    else:
        print(1, end="")
print()
n = int(input())
s = input()
q = int(input())
k = [int(m) for m in input().split()]
dmc = []
dc = 0
for i in range(n):
    if s[i] == "D" or s[i] == "M" or s[i] == "C":
        dmc.append([s[i], i])
    if s[i] == "D":
        dc += 1
d = []
m = []
rm = []
c = []
for h in range(dc):
    m.append(0)
    rm.append(0)
    c.append(0)
for i in range(q):
    for j in range(len(dmc)):
        if dmc[j][0] == "D":
            d.append(dmc[j][1])
        if dmc[j][0] == "M":
            for v in range(len(d)):
                if dmc[j][1] - d[v] < k[i]:
                    rm[v] += 1
        if dmc[j][0] == "C":
            for v in range(len(d)):
                if dmc[j][1] - d[v] < k[i]:
                    c[v] += 1
                    m[v] = rm[v]
    combined1 = [x * y for (x, y) in zip(m, c)]
    print(sum(combined1))
    d = []
    m = []
    rm = []
    c = []
    for h in range(dc):
        m.append(0)
        rm.append(0)
        c.append(0)
n = int(input())
s = input()

ans = 0
p = 0
q = 0
sai = 0
v = 0
w = 0
pairs = []
for i in range(n - 1, -1, -1):
    if s[i] == "." and sai == 0:
        p = 0
        q = 0
        p += 1
        v = 1
        sai = 1
    elif s[i] == "." and v == 0:
        pairs.append([q, p])
        p = 0
        q = 0
        w = 0
        p += 1
        v = 1
    elif s[i] == "." and v == 1:
        p += 1
    elif s[i] == "#" and w == 0 and sai == 1:
        v = 0
        q += 1
        w = 1
    elif s[i] == "#" and w == 1:
        q += 1
pairs.append([q, p])
rp = []
for i in range(len(pairs)):
    rp.append(pairs[-i-1])
d = []
prp = []
p0 = 0
p1 = 0
for i in range(len(rp)):
    p0 += rp[i][0]
    p1 += rp[i][1]
    prp.append([p0, p1])
for i in range(len(prp)):
    d.append(prp[i][0] + prp[len(prp) - 1][1] - prp[i][1])
d.append(prp[len(prp) - 1][0])
d.append(prp[len(prp) - 1][1])
print(min(d))

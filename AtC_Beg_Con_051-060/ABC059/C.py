n = int(input())
a = input().split()
a = [int(m) for m in a]
q = []
k = 0
kco = 0
#+-
for i in range(n):
    if i == 0:
        if a[i] > 0:
            q.append(a[i])
        else:
            q.append(1)
            kco += 1 - a[i]
        k += q[i]
    else:
        k += a[i]
        if i % 2 != 0:
            if k < 0:
                q.append(a[i])
            else:
                q.append(a[i]-k-1)
                kco += k + 1
            k += q[i] - a[i]
        if i % 2 == 0:
            if k > 0:
                q.append(a[i])
            else:
                q.append(a[i]-k+1)
                kco += -k + 1
            k += q[i] - a[i]
xco = kco
q = []
k = 0
kco = 0
#-+
for i in range(n):
    if i == 0:
        if a[i] < 0:
            q.append(a[i])
        else:
            q.append(-1)
            kco += a[i] + 1
        k += q[i]
    else:
        k += a[i]
        if i % 2 == 0:
            if k < 0:
                q.append(a[i])
            else:
                q.append(a[i]-k-1)
                kco += k + 1
            k += q[i] - a[i]
        if i % 2 != 0:
            if k > 0:
                q.append(a[i])
            else:
                q.append(a[i]-k+1)
                kco += -k + 1
            k += q[i] - a[i]
yco = kco
print(min(xco, yco))


"""p = 0
b = []
c = []
for i in range(n):
    p += a[i]
    if i % 2 == 0:
        b.append(p)
    else:
        c.append(p)
#b+c-のとき
bmin = min(b)
cmax = max(c)
bco1 = 0
cco1 = 0
if bmin <= 0:
    bco1 = 1 - bmin
if cmax >= 0:
    cco1 = cmax + 1
d = bco1 + cco1
#b-c+のとき
bmax = max(b)
cmin = min(c)
bco2 = 0
cco2 = 0
if bmax >= 0:
    bco2 = bmax + 1
if cmax >= 0:
    cco2 = 1 - cmin
e = bco2 + cco2

f = min(d, e)
print(f)"""
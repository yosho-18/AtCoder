import copy
n = int(input())
v = input().split()

x = []
y = []

for i in range(n):
    if i % 2 == 0:
        x.append(v[i])
    else:
        y.append(v[i])

x.sort()
y.sort()

q = []
r = []
s = []
t = []
countx = 1
county = 1

for j in range(int(n / 2)):
    if x[j - 1] == x[j] and j != 0:
        countx += 1
    if j == n / 2 - 1:
        s.append(countx)
        q.append(x[j])
        countx = 1
    elif x[j - 1] != x[j] and j != 0:
        s.append(countx)
        q.append(x[j - 1])
        countx = 1


for k in range(int(n / 2)):
    if y[k - 1] == y[k] and k != 0:
        county += 1
    if k == n / 2 - 1:
        t.append(county)
        r.append(y[k])
        county = 1
    elif y[k - 1] != y[k] and k != 0:
        t.append(county)
        r.append(y[k - 1])
        county = 1
s2 = copy.deepcopy(s)
t2 = copy.deepcopy(t)
#a = [int(m) for m in a]
s2.sort(reverse=True)
t2.sort(reverse=True)
sc = -1
tc = -1
sk = 0
tk = 0

ssym = 0
for i in s2:
    if sc == -1:
        sk = i
    elif sc == 0:
        sk = i
        ssym = 1
        break
    sc += 1
if sc == 0 and ssym == 0:
    sk = 0

tsym = 0
for i in t2:
    if tc == -1:
        tk = i
    elif tc == 0:
        tk = i
        tsym = 1
        break
    tc += 1
if tc == 0 and tsym == 0:
    tk = 0

if q[s.index(max(s))] != r[t.index(max(t))]:
    print(n - max(s) - max(t))
else:
    if sk >= tk:
        print(n - sk - max(t))
    else:
        print(n - max(s) - tk)

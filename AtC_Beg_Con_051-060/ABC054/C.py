import itertools
n, m = map(int, input().split())
c = []
for i in range(m):#h:高さ
    c.append([int(m) for m in input().split()])
c.sort()
d = []
for i in range(n):
    d.append([])
for i in range(m):
    for k in range(n):
        if c[i][0] == k + 1:
            d[k].append(c[i][1])
        if c[i][1] == k + 1:
            d[k].append(c[i][0])
nli = [i + 1 for i in range(1, n)]
ans = 0
for path in itertools.permutations(nli, n - 1):
    for i in range(len(path) - 1):
        if i == 0:
            if path[i] in d[0]:
                if path[i + 1] in d[path[i] - 1]:
                    pass
                    if i == len(path) - 2:
                        ans += 1
                else:
                    break
            else:
                break
        else:
            if path[i + 1] in d[path[i] - 1]:
                pass
                if i == len(path) - 2:
                    ans += 1
            else:
                break
if n == 2:
    ans += 1
print(ans)
"""#深さ優先探索
labelli = [-1]*n
label = 0
v = 0
labelli[0] = label
p = 0
back = []
backnumber = []
q = 0
count = 0
for h in range(len(c1)):

    for i in range(len(c2)):
        for j in range(len(c3)):
            for k in range(len(c4)):
                for l in range(len(c5)):
                    for p in range(len(c6)):
                        for q in range(len(c7)):"""




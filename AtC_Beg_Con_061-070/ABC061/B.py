import collections
from collections import defaultdict
n, m = map(int, input().split())
s = []
for i in range(m):#h:高さ
    s.append([int(m) for m in input().split()])

d = defaultdict(int)
#e = defaultdict(int)
for i in range(1, n + 1):
    d[i] = 0
for i in range(m):
    d[s[i][0]] += 1
    d[s[i][1]] += 1
for i in range(1, n + 1):
    print(d[i])

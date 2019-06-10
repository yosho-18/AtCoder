import collections
n = int(input())
s = []
for i in range(n):
    s.append(input())
m = int(input())
t = []
for i in range(m):
    t.append(input())

cs = collections.Counter(s)
ct = collections.Counter(t)
#print(cs)
#l = max(n, m)
count = []
count.append(0)
for i in range(n):
    count.append(cs[s[i]] - ct[s[i]])

for j in range(m):
    count.append(cs[t[j]] - ct[t[j]])

print(max(count))
"""from statistics import mode

tmp_list = [1, 1, 1, 1, 0, 1, 1]
print(mode(tmp_list))
u = max(s)"""
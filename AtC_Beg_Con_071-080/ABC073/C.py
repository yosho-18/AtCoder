import collections
n = int(input())
a = []
for i in range(n):
    a.append(input())
# [d1, d2, d3, ..., dN]
a = [int(m) for m in a]#int型に直す
c = collections.Counter(a)
count = 0
for i in c:
    if c[i] % 2 != 0:
        count += 1
print(count)
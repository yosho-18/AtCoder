import collections
n = int(input())
a = input().split()
a = [int(m) for m in a]
a.sort()
c = collections.Counter(a)
count = 0
for i in c:
    if c[i] % 2 == 0:
        count += 1
if count % 2 == 0:
    print(len(c))
else:
    print(len(c) - 1)

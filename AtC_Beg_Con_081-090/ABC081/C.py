import collections

n, k = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
a.sort()
c = collections.Counter(a)

values, counts = zip(*c.most_common()[::-1])

count = 0
i = 0

if len(c) <= k:
    print(0)
    exit()
else:
    for j in counts:
        if i >= 0 and i <= len(counts) - 1 - k:
            count += j
        i += 1

print(count)

"""for i, name in enumerate(l, 1):
    print('{:03}_{}'.format(i, name))"""

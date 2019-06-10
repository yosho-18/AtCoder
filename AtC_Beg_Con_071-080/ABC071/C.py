import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
d = {}
for i in c:
    if c[i] >= 2:
        d[i] = c[i]

if d != {}:
    dct = sorted(d.items(), key=lambda x: -x[0])
    if len(d) == 1:
        if dct[0][1] >= 4:
            print(dct[0][0] ** 2)
        else:
            print(0)
    else:
        if dct[0][1] >= 4:
            print(dct[0][0] ** 2)
        else:
            print(dct[0][0] * dct[1][0])
else:
    print(0)
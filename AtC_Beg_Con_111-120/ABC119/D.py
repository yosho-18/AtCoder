from bisect import bisect_right
a, b, q = map(int, input().split())
INF = 10 ** 18
s = [-INF]
for i in range(a):
    s.append(input())
s.append(INF)
s = [int(m) for m in s]#int型に直す
t = [-INF]
for i in range(b):
    t.append(input())
t.append(INF)
t = [int(m) for m in t]#int型に直す
x = []
for i in range(q):
    x.append(input())
x = [int(m) for m in x]#int型に直す

for i in range(q):
    b, d = bisect_right(s, x[i]), bisect_right(t, x[i])
    a, c = b - 1, d - 1
    res = INF
    for j in [a, b]:
        for k in [c, d]:
            res = min(res, abs(x[i] - s[j]) + abs(s[j] - t[k]), abs(x[i] - t[k]) + abs(t[k] - s[j]))
    print(res)
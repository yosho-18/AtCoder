q, h, s, d = map(int, input().split())
n = int(input())
q1 = q / 0.25
h1 = h / 0.5
s1 = s / 1
d1 = d / 2
minx = min(q1, h1, s1, d1)
a = [[q1, 0.25], [h1, 0.5], [s1, 1], [d1, 2]]
a.sort()
if n % 2 != 0 and a[0][1] == 2:
    print(int((n - 1) // 2 * d) + int(a[1][0]))
else:
    if minx == d1:
        print(int(d * n // 2))
    else:
        print(int(minx * n))
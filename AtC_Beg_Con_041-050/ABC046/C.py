import math
n = int(input())
c = []
d = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])
    d.append([])
d[0].append(c[0][0])
d[0].append(c[0][1])

def f(x,y):
    return x//y + (1 if x%y > 0 else 0)
"""def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm_base(x, y):
    return (x * y) // gcd(x, y)"""

for i in range(1, n):
    """if d[i - 1][0] <= c[i][0] and d[i - 1][1] <= c[i][1]:
        d[i].append(c[i][0])
        d[i].append(c[i][1])
    elif d[i - 1][0] <= c[i][0] and d[i - 1][1] > c[i][1]:
        d[i].append(math.ceil(d[i - 1][1] / c[i][1]) * c[i][0])
        d[i].append(math.ceil(d[i - 1][1] / c[i][1]) * c[i][1])
    elif d[i - 1][0] > c[i][0] and d[i - 1][1] <= c[i][1]:
        d[i].append(math.ceil(d[i - 1][0] / c[i][0]) * c[i][0])
        d[i].append(math.ceil(d[i - 1][0] / c[i][0]) * c[i][1])
    else:"""
    #zz = max(math.ceil(d[i - 1][0] / c[i][0]), math.ceil(d[i - 1][1] / c[i][1]))
    zz = max(f(d[i - 1][0], c[i][0]),f(d[i - 1][1], c[i][1]))
    d[i].append(c[i][0] * zz)
    d[i].append(c[i][1] * zz)
    """p1 = lcm_base(d[i - 1][0], c[i][0])
    xx = p1 // c[i][0]
    p2 = c[i][1] * xx
    p1 = math.ceil(d[i - 1][1] / p2) * p1
    p2 = math.ceil(d[i - 1][1] / p2) * p2

    q2 = lcm_base(d[i - 1][1], c[i][1])
    yy = q2 // c[i][1]
    q1 = c[i][0] * yy
    q2 = math.ceil(d[i - 1][0] / q1) * q2
    q1 = math.ceil(d[i - 1][0] / q1) * q1

    if p1 + p2 >= q1 + q2:
        d[i].append(q1)
        d[i].append(q2)
    else:
        d[i].append(p1)
        d[i].append(p2)"""
    print(d[i][0], d[i][1])
print(d[n - 1][0] + d[n - 1][1])#ceil関数使えない10.00000000000000001 = 10
import collections
import math
n, m = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
b = [0]
t = 0
for i in range(n):
    t += a[i]
    b.append(t)
mod = m
c = []
for i in range(n + 1):
    c.append(b[i] % mod)

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ans = 0
col = collections.Counter(c)
for i in col:
    if col[i] != 1:
        ans += comb(col[i], 2)
print(ans)

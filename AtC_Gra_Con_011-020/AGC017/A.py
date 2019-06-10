import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n, p = map(int, input().split())
a = [int(m) for m in input().split()]
k = 0
for i in range(n):
    if a[i] % 2 == 0:
        k += 1

if p == 1:
    tmp = 0
    for i in range(1, n - k + 1, 2):
        tmp += comb(n - k, i)
    print((2 ** k) * tmp)
else:
    tmp = 0
    for i in range(0, n - k + 1, 2):
        tmp += comb(n - k, i)
    print((2 ** k) * tmp)
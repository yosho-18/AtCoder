import numpy as np
#import numpy as np
import itertools
n = int(input())
a = []
for i in range(n):
    a.append(input())
# [d1, d2, d3, ..., dN]
a = [int(m) for m in a]

a.sort()
if n % 2 == 0:
    small = []
    big = []
    for i in range(n):
        if i < n // 2:
            small.append(a[i])
        else:
            big.append(a[i])
    print(2 * (sum(big) - sum(small)) - big[0] + small[n // 2 - 1])
else:
    small = []
    big = []
    for i in range(n):
        if i < n // 2:
            small.append(a[i])
        elif i > n // 2:
            big.append(a[i])
    print(max(2 * (sum(big) - sum(small)) - big[0] + a[n // 2], 2 * (sum(big) - sum(small)) + small[n // 2 - 1] - a[n // 2]))
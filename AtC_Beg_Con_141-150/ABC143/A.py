import itertools
import collections
import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n = int(input())
a = [0] + [int(m) for m in input().split()]
accua = itertools.accumulate(a)
#accua.append(0)
dict = collections.Counter(accua)
ans = 0
for i in dict:
    if dict[i] >= 2:
        ans += comb(dict[i], 2)
print(ans)

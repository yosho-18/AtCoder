import math
from collections import defaultdict
# 0以上整数x「未満」の素数をリストに格納して返す
n = int(input())
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0  # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]
pr = primes(100)
q = math.factorial(n)
di = {}
di = defaultdict(int)
for i in pr:
    while q % i == 0:
        q = q // i
        di[i] += 1
co = 0
do1 = 0
eo1= 0
do2 = 0
eo2= 0
do3 = 0
eo3= 0
for k in di:
    if di[k] >= 24:
        do1 += 1
    if di[k] >= 2:
        eo1 += 1
if do1 >= 1 and eo1 >= 2:
    co += do1 * (eo1 - 1)
for k in di:
    if di[k] >= 14:
        do2 += 1
    if di[k] >= 4:
        eo2 += 1
if do2 >= 1 and eo2 >= 2:
    co += do2 * (eo2 - 1)
for k in di:
    if di[k] >= 4:
        do3 += 1
    if di[k] >= 2:
        eo3 += 1
if do3 >= 2 and eo3 >= 3:
    co += comb(do3,2) * (eo3 - 2)
for k in di:
    if di[k] >= 74:
        co += 1
print(co)
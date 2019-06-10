import math
from collections import defaultdict
# 0以上整数x「未満」の素数をリストに格納して返す
n, p = map(int, input().split())

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
#pr = primes(p + 1)
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

pr = prime_factors(p)
di = {}
di = defaultdict(int)
for i in pr:
    while p % i == 0:
        p = p // i
        di[i] += 1

ans = 1
ww = 1
for i in di:
    while True:
        if di[i] >= ww * n:
            ans *= i
            ww += 1
        else:
            ww = 1
            break
print(ans)
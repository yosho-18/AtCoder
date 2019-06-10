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
pr = primes(n + 1)
q = math.factorial(n)
di = {}
di = defaultdict(int)
for i in pr:
    while q % i == 0:
        q = q // i
        di[i] += 1

ans = 1
mod = 10 ** 9 + 7
for i in di:
    ans *= di[i] + 1
    ans %= mod
print(ans)
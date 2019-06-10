import math
from collections import defaultdict

n, m = map(int, input().split())

"""def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0  # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

pr = primes(m + 1)
di = {}
di = defaultdict(int)
for i in pr:
    while m % i == 0:
        m = m // i
        di[i] += 1"""
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

pr = prime_factors(m)
di = {}
di = defaultdict(int)
for i in pr:
    while m % i == 0:
        m = m // i
        di[i] += 1

"""def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))"""
mod = 10 ** 9 + 7
MAX_N = 10 ** 5 + 100
factorial = [1] * MAX_N
#事前に階上テーブルを用意
def calc_factorial():
    for i in range(1, MAX_N):
        factorial[i] = i * factorial[i - 1] % mod

def comb(n, k):
    a = factorial[n] % mod
    b = (factorial[k] * factorial[n - k]) % mod
    b_ = pow(b, mod - 2, mod)
    return (a * b_) % mod


# 階乗を用意
calc_factorial()

ans = 1

for i in di:
    ans = ans * comb(di[i] + n - 1, di[i]) % mod
print(ans)
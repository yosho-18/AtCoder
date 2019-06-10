from collections import defaultdict
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
import math
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

pr = primes(k)#k未満の素数をリストで渡す

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

    print(prime_factors(123123200001))

q = math.factorial(n)
di = {}
di = defaultdict(int)
for i in pr:
    while q % i == 0:
        q = q // i
        di[i] += 1


"""import sympy
# mを素因数分解して辞書にする
di = sympy.factorint(m)"""
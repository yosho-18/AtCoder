n = int(input())
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
primeslist = primes(55556)
l_n_str = [str(n) for n in primeslist]
pl1 = []
for i in range(len(primeslist)):
    if l_n_str[i][-1] == "1":
        pl1.append(primeslist[i])

for i in range(n):
    print(pl1[i], "" , end = "")
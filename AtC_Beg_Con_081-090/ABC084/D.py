import math
import copy

# 0以上整数x「未満」の素数をリストに格納して返す
def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

def realprimes(y):
    Y = primes(y)
    t = int((y + 1) / 2)
    bestprime = []

    for prime in Y:
        if prime != 2:
            prime2 = (prime + 1)//2
            pw = 0
            for i in range(2,int(math.sqrt(prime2)) + 2):
                if prime2 == 2:
                    break
                elif prime2 % i == 0:
                    pw = 1
                    break
            if pw == 0:
                bestprime.append(prime)

    T = bestprime
    V = set(Y) & set(T)
    return list(V)
W = realprimes(10**5 - 1)
W.sort()
W.append(10**5)
q = int(input())
s = []
for i in range(q):#h:高さ
    s.append([int(m) for m in input().split()])

j = 0
Z = []
for i in range(10 ** 5):
    if i < W[j]:
        Z.append(j)
    else:
        j += 1
        Z.append(j)

for i in range(q):
    if Z[s[i][0]] != Z[s[i][0] - 1]:
        print(Z[s[i][1]] - Z[s[i][0]] + 1)
    else:
        print(Z[s[i][1]] - Z[s[i][0]])


#ALL = [i + 1 for i in range(10**5)]
#ALL2 = copy.deepcopy(ALL)
"""p = 0
p2 = 0
c = 0
c2 = 0"""
"""for i in range(q):
    ALL = ALL2[s[i][0] - 1:s[i][1]]
    length = len(set(ALL) & set(W))
    print(length)
    ALL = ALL2"""
"""while p == 0:
        if s[i][0] + c > s[i][1]:
            cut1 = 0
            break
        if s[i][0] + c in W:
            cut1 = W.index(s[i][0] + c)
            p = 1
        else:
            c += 1
    p = 0
    c = 0
    while p2 == 0:
        if s[i][1] - c2 < s[i][0]:
            cut2 = -1
            break
        if s[i][1] - c2 in W:
            cut2 = W.index(s[i][1] - c2)
            p2 = 1
        else:
            c2 += 1
    p2 = 0
    c2 = 0
    print(cut2 - cut1 + 1)"""



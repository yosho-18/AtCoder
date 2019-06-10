from collections import Counter
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
N, K = map(int, input().split())
A = sorted([gcd(a, K) for a in list(map(int, input().split()))])

C = Counter(A)
ans = 0

for a in C.keys():
    for b in C.keys():
        if a * b % K == 0:
            if a == b:
                ans += C[a] * (C[b] - 1)

            if a != b:
                ans += C[a] * C[b]

print(ans // 2)

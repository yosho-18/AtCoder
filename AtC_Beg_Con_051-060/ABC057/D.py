import math
n, a, b = map(int, input().split())
v = [int(m) for m in input().split()]
v.sort(reverse=True)

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


k = 0
l = 0
maxli = []
for i in range(a, b + 1):
    w = v[:i]
    avgv = sum(w) / i
    x = v[i - 1]
    for u in range(len(w) - 1, -1, -1):
        if u == len(w) - 1:
            l = 1
        else:
            if v[u] == v[u + 1]:
                l += 1
            else:
                break
    for j in range(i - 1, n):
        if j == i - 1:
            k = 1
        else:
            if v[j] == v[j - 1]:
                k += 1
            else:
                break
    k -= 1
    maxli.append([avgv, comb(l + k, l)])

S = 0
K = 0
maxli.sort(reverse=True)
for i in range(len(maxli)):
    if i == 0:
        S = maxli[i][0]
        K = maxli[i][1]
    else:
        if maxli[i][0] == maxli[i - 1][0]:
            K += maxli[i][1]
        else:
            break
print(S)
print(K)
n = int(input())
mod = 1000000007
kli = [0]
nli = []
for i in range(1, n + 1):
    k = n // i
    #kli.append(k)
    nli.append((i ** 10 - (i - 1) ** 10) * (k ** 10))
print((sum(nli) - (sum(kli))) % mod)
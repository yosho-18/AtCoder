n = int(input())
t = 1
mod = 10**9 + 7
for i in range(1, n + 1):
    t *= i
    t = t % mod
print(t)
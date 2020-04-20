n, k = [int(m) for m in input().split()]
mod = 10 ** 9 + 7

ans = 0
for i in range(k, n + 2):
    ans += (n * (n + 1) // 2 - (n - i) * (n - i + 1) // 2) - i * (i - 1) // 2 + 1
    ans %= mod

print(ans)
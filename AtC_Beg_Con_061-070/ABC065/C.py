import math
n, m = map(int, input().split())
mod = 10 ** 9 + 7
if abs(n - m) > 1:
    print(0)
elif abs(n - m) == 1:
    print(math.factorial(n) * math.factorial(m) % mod)
elif n == m:
    print(2 * math.factorial(n) * math.factorial(m) % mod)
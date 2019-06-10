a, b, c = map(int, input().split())
mod = 10 ** 9 + 7
ka = a % mod
kd = ka * b % mod
ke = kd * c % mod
print(ke)
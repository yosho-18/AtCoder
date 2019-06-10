h, w, a, b = map(int, input().split())
mod = 10 ** 9 + 7
MAX_N = 2 * 10 ** 5
factorial = [1] * MAX_N
#事前に階上テーブルを用意
def calc_factorial():
    for i in range(1, MAX_N):
        factorial[i] = i * factorial[i - 1] % mod

def comb(n, k):
    a = factorial[n] % mod
    b = (factorial[k] * factorial[n - k]) % mod
    b_ = pow(b, mod - 2, mod)
    return (a * b_) % mod


# 階乗を用意
calc_factorial()
all = comb(h + w - 2, h - 1)
sub = 0
for j in range(1, b + 1):
    sub += comb(h - a - 1 + j - 1, j - 1) * comb(a - 1 + w - j, w - j)
    sub = sub % mod
if all - sub <= 0:
    print(all - sub + mod)
else:
    print(all - sub)
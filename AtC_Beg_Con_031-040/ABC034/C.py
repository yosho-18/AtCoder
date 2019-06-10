h, w = map(int, input().split())
mod = 10 ** 9 + 7
MAX_N = 3 * 10 ** 5 + 100
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

print(comb(h + w - 2, h - 1))
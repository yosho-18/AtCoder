from functools import reduce
import math
#nHr=n+r-1Cr
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
def gcd(*numbers):
    return reduce(gcd, numbers)
def gcd_list(numbers):
    return reduce(gcd, numbers)
print(gcd(27, 18, 9))
# 9
print(gcd(27, 18, 9, 3))
# 3
print(gcd([27, 18, 9, 3]))
# [27, 18, 9, 3]
print(gcd(*[27, 18, 9, 3]))
# 3
print(gcd_list([27, 18, 9, 3]))
# 3

def lcm_base(x, y):
    return (x * y) // gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
#print(lcm(27, 18, 9, 3))
# 54
#print(lcm(27, 9, 3))
# 27
#print(lcm(*[27, 9, 3]))
# 27


mod = 10 ** 9 + 7
MAX_N = 10 ** 5 + 100
factorial = [1] * MAX_N
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
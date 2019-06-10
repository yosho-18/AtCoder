from functools import reduce

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_list(numbers):
    return reduce(gcd, numbers)

print(gcd_list([27, 18, 9, 3]))
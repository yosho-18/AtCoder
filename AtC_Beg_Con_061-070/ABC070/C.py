from functools import reduce

n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
t = [int(m) for m in d]

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

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

print(lcm_list(t))

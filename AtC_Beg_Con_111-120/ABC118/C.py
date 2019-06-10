from functools import reduce
n = int(input())
a = [int(m) for m in input().split()]
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
def gcd_list(numbers):
    return reduce(gcd, numbers)
a.sort()
new = [a[0]]
for i in range(1, n):
    new.append(a[i] % a[0])

new.sort()

k = gcd_list(new)
for i in range(n):
    if new[i] % k != 0:
        print(1)
        exit()
print(gcd_list(new))
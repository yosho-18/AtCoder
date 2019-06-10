n = int(input())
a = [int(m) for m in input().split()]
a.sort()
m0 = a[0]
m1 = a[1]
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors



mm0 = make_divisors(m0)
mm1 = make_divisors(m1)
mm = mm0 + mm1
mm.sort()
si = 0
candi = 0
for g in mm:
    si = 0
    for i in range(n):
        if a[i] % g != 0:
            si += 1
            if si == 2:
                break
    else:
        candi = g
print(candi)
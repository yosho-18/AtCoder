n = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
                pass

    # divisors.sort()
    return divisors

yakusuli = make_divisors(n)

ans = 0

for i in yakusuli:
    if i < n // i - 1:
        ans += n // i - 1

print(ans)
#1000000000000
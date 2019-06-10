n, k = map(int, input().split())
count = 0
for b in range(1, n + 1):
    if k < b:
    #a < bを考える
        if k != 0:
            count += b - k
        else:
            count += b - 1
    # a > bを考える
        p = n // b - 1
        q = n % b - k + 1 if n % b - k + 1 > 0 else 0
        count += p * (b - k) + q
print(count)


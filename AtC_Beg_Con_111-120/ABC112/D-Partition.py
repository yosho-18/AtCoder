n, m = map(int, input().split())
p = int(m / n)

if n > 100:
    for i in range(p, 0, -1):
        if m % i == 0:
            print(i)
            break
else:
    for i in range(n, m + 1):
        if m % i == 0:
            print(int(m / i))
            break




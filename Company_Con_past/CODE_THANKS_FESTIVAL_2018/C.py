n = int(input())
a = input().split()
x = [int(m) for m in a]
x.sort()
b = []
for i in range(1, n):
    b.append(abs(x[i] - x[i - 1]))

mul = []
for i in range(1, n):
    mul.append(i * (n - i))

ans = 0
for i in range(n - 1):
    ans += b[i] * mul[i]

print(ans)
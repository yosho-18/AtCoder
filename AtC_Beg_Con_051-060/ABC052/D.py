#横にn個入力
n, a, b = map(int, input().split())
x = input().split()
x = [int(m) for m in x]

ans = 0
for i in range(1, n):
    k = x[i] - x[i - 1]
    if k * a < b:
        ans += k * a
    else:
        ans += b

print(ans)
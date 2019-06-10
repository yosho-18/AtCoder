r, n, m = map(int, input().split())
ans = 0
p = (2 * r) / n
for i in range(1, n + m):
    if i - m < 0:
        ans += 2 * (-(abs(n / 2 - i) * p) ** 2 + r ** 2) ** 0.5
    elif i < n:
        if -(abs(n / 2 - i + m) * p) ** 2 + r ** 2 >= 0:
            ans += 2 * max((-(abs(n / 2 - i) * p) ** 2 + r ** 2) ** 0.5, (-(abs(n / 2 - i + m) * p) ** 2 + r ** 2) ** 0.5)
        else:
            ans += 2 * (-(abs(n / 2 - i) * p) ** 2 + r ** 2) ** 0.5
    else:
        ans += 2 * (-(abs(n / 2 - i + m) * p) ** 2 + r ** 2) ** 0.5
print(ans)
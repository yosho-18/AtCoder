n = int(input())
ans = 0
for a in range(10 ** 5):
    if a ** 2 <= n:
        ans = a
    else:
        break
print(ans)
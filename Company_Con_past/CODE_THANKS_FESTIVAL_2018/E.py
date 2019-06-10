t = int(input())

a = [0] + [int(m) for m in input().split()]
mod = 10 ** 9 + 7
A = max(a)

ans = 0
dec = 0
for i in range(1, 400 + 1):
    if 2 ** (i - 1) < A:
        ans = (ans + 2 ** (i - 1)) % mod
    elif i > t:
        dec += 1
        if A - dec > 0:
            ans = (ans + A - dec) % mod
    else:
        ans = (ans + A) % mod
print(ans)
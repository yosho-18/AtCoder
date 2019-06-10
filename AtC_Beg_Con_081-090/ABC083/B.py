n, a, b = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    strli = list(str(i))
    l_n_str = [int(n) for n in strli]
    sumstr = sum(l_n_str)
    if a <= sumstr <= b:
        ans += i
print(ans)
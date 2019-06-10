#横にn個入力
n, a, b = map(int, input().split())
if a + b <= n:
    print(min(a,b),0)
else:
    print(min(a,b),a + b - n)
from itertools import combinations
n, k = map(int, input().split())
a = [int(m) for m in input().split()]
nums = a
S = 0
Ans = 0
Ans = float("INF")
for balls in combinations(nums, k):
    S = sum(balls)
    ans = 0
    while S != 0:#文字型にするとPyPyでは遅くなるので，数値型で処理する．
        if S % 10 >= 5:
            ans += S % 10 - 4
        else:
            ans += S % 10
        S //= 10
    Ans = min(Ans, ans)
print(Ans)
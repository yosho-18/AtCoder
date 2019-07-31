import sys
from bisect import insort_left

def wi(): return list(map(int, sys.stdin.readline().split()))

n, k = wi()
x = wi()
# newx = [[x[i], i + 1] for i in range(n)] # 二次元配列だと遅いので一次元＋辞書で書き直した
age_num = {}
for cnt, age in enumerate(x, 1):
    age_num[age] = cnt

y = x[:k]
z = x[k:]
y.sort()  # 二分探索に単調性は必須
print(age_num[y[k - 1]])  # k番目のひとが何歳かをまず調べ，その年の人が何位かを調べ，それに変換する．

for cnt, age in enumerate(z):
    insort_left(y, age)
    print(age_num[y[k - 1]])
    y.pop(-1)  # 最後尾（k+1番目）は絶対にこれからk番目になることはないので，ここで削除しておく，これによりinsort_leftの計算量を減らす
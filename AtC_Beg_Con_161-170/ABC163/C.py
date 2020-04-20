from collections import defaultdict

n = int(input())
a = [int(m) for m in input().split()]
n_buka = defaultdict(int)  # 辞書を作成，デフォルトは0
# d = defaultdict(lambda: float("INF"))

for i in range(n - 1):
    n_buka[a[i]] += 1

for i in range(1, n + 1):
    print(n_buka[i])
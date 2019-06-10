n, m = map(int, input().split())
kl = []
for i in range(n):#h:高さ
    kl.append([int(m) for m in input().split()])
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [i for i in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n + 1)

    # 検索
    # 根ならその番号を返す
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            # 走査していく過程で親を書き換える
            self.par[x] = self.find(self.par[x])
            return self.par[x]

        # 併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
        # 木の高さが同じなら片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

u = UnionFind(n + m)
for i in range(n):
    ki = kl[i][0]
    for j in range(1, ki + 1):
        u.union(m + i + 1, kl[i][j])
print(('NO', 'YES')[all(u.same_check(m + 1, m + i + 1) for i in range(n))])



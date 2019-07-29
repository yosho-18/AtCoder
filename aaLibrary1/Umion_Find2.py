class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [-1 for i in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        """self.rank = [0] * (n + 1)"""


    # 検索
    # 根ならその番号を返す
    def find(self, x):
        if self.par[x] < 0:
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
        if x != y:
            if self.par[x] < self.par[y]:#par<0の小さい方に合わせる
                self.par[y] += self.par[x]
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
            # 木の高さが同じなら片方を1増やす
                """if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1"""

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]
u = UnionFind(6)
u.union(0,2)
u.union(4,3)
u.union(2,1)
u.union(5,4)
u.union(5,6)
u.union(2,4)
u = UnionFind(n)
for i in range(m):
    u.union(ab[i][0], ab[i][1])



#print(u.parent)
a = [5,3,1,4,2,6]
count = 0
for i in range(6):
    if u.same_check(i, (a[i] - 1)):
        count += 1
print(count)


class UnionFindTree:
    def __init__(self, size):
        self.parent = list(range(size))
        self.age = [0] * size

    def find_root(self, x):
        if self.parent[x] == x:
            return x, 0
        else:
            self.parent[x], d = self.find_root(self.parent[x])
            self.age[x] += d
            return self.parent[x], self.age[x]

    def union(self, x, y, d):
        r1, d1 = self.find_root(x)
        r2, d2 = self.find_root(y)
        if r1 != r2:
            self.parent[r2] = r1
            self.age[r2] = (d1 - d2) + d
        else:
            if (d2 - d1) != d:
                return False
        return True
    
"""class UnionFind:
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
"""
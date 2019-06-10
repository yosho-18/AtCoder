import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n, m = map(int, input().split())
c = []
for i in range(m):#h:高さ
    c.append([int(m) for m in input().split()])
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [i for i in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n + 1)
        self.le = [set() for i in range(n+1)]

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
        self.le[self.find(x)].add(x)
        self.le[self.find(y)].add(y)
        x = self.find(x)
        y = self.find(y)
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.le[x] = self.le[x] | self.le[y]
            self.le[y] = self.le[y] | self.le[x]
        else:
            self.par[y] = x
            self.le[y] = self.le[y] | self.le[x]
            self.le[x] = self.le[x] | self.le[y]

        # 木の高さが同じなら片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return len(self.le[self.find(x)])
ansli = [((n - 1) * n) // 2]
alln = ((n - 1) * n) // 2
setn = set()
u = UnionFind(n)
aq = 0
for i in range(m - 1, 0, -1):
    if c[i][0] not in setn and c[i][1] not in setn:
        u.union(c[i][0], c[i][1])
        setn.add(c[i][0])
        setn.add(c[i][1])
        aq += 1
    elif c[i][0] in setn and c[i][1] not in setn:
        aq += u.size(c[i][0])
        u.union(c[i][0], c[i][1])
        setn.add(c[i][1])
    elif c[i][0] not in setn and c[i][1] in setn:
        aq += u.size(c[i][1])
        u.union(c[i][0], c[i][1])
        setn.add(c[i][0])
    else:
        if u.same_check(c[i][0], c[i][1]):
            u.union(c[i][0], c[i][1])
        else:
            aq += u.size(c[i][1]) * u.size(c[i][0])
            u.union(c[i][0], c[i][1])
    ansli.append(alln - aq)
for i in reversed(range(m)):
    print(ansli[i])
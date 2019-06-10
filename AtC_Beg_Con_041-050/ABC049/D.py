import collections
N,K,L = map(int, input().split())
p = []
q = []
for i in range(K):#h:高さ
    pi, qi = map(int, input().split())
    p.append(pi)
    q.append(qi)
r = []
s = []
for i in range(L):#h:高さ
    ri, si = map(int, input().split())
    r.append(ri)
    s.append(si)

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

u = UnionFind(N)
for i in range(K):
    u.union(p[i],q[i])


u2 = UnionFind(N)
for i in range(L):
    u2.union(r[i],s[i])

li = [None]*(N)
liw = [None]*(N)
for i in range(N):
    li[i] = (u.find(i + 1), u2.find(i + 1), i + 1)
    liw[i] = (u.find(i + 1), u2.find(i + 1))
#li.sort(key=lambda x:(x[0], x[1]))

liws = collections.Counter(liw)

ansli = [0]*(N+1)
for i in range(N):
    ansli[i + 1] = liws[(li[i][0], li[i][1])]

for i in range(1, N + 1):
    print(ansli[i], "", end="")
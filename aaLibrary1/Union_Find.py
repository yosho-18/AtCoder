class UnionFind():
    #負の値はルートで集合の個数
    #正の値は次の要素を返す
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]

    #集合の代表を求める
    def find(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    #併合
    def union(self,x,y):
        s1 = self.find(x)#根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:#根が異なる場合
            if self.table[s1] != self.table[s2]:#グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                else:
                    self.table[s1] = s2
            else:
                #グラフの長さが同じ場合,どちらを根にしても変わらない
                #その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
        return

class UnionFind2(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]


    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])


    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

u = UnionFind2(5)
u.unite(0,2)
u.unite(4,3)
print(u.parent)
a = [5,3,1,4,2]
count = 0
for i in range(5):
    if u.parent[i] == u.parent[a[i] - 1]:
        count += 1
print(count)

"""In[113]: u = UnionFind(10)

In [114]: u.unite(1,2)

In [115]: u.unite(3,2)

In [116]: u.unite(5,6)

In [117]: u.parent
Out[117]: [0, 1, 1, 1, 4, 5, 5, 7, 8, 9]

In [119]: u.rank
[0, 1, 0, 0, 0, 1, 0, 0, 0, 0]"""
u = UnionFind(n)
for i in range(m):
    u.union(s[i][0] - 1, s[i][1] - 1)
    k = u.table
k = u.table
#rt = u.find()
count = 0
for i in range(n):
    if u.find(i) == u.find(a[i] - 1):
        count += 1
print(count)
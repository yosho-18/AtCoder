import copy
n = int(input())
d = []
for i in range(n - 1):#h:高さ
    d.append([int(m) for m in input().split()])
q, k = map(int, input().split())
z = []
for i in range(q):#h:高さ
    z.append([int(m) for m in input().split()])

for i in range(n - 1):
    d[i][0] -= 1
    d[i][1] -= 1
for i in range(q):
    z[i][0] -= 1
    z[i][1] -= 1
def BFS(k, edges, N):
  roots=[ [] for i in range(N)]
  for a,b,c in edges:
    roots[a]+=[(b,c)]
    roots[b]+=[(a,c)]
  dist=[-1]*N
  stack=[]
  stack.append(k)
  dist[k]=0
  while stack:
    label=stack.pop(-1)
    for i,c in roots[label]:
      if dist[i]==-1:
        dist[i]=dist[label]+c
        stack+=[i]
  return dist

root = BFS(k - 1, d, n)

for i in range(q):
    print(root[z[i][0]] + root[z[i][1]])
"""
f = {}
for i in range(1, n + 1):
    if i != k:
        f[i] = 0
ar = []
pre = {}

for i in e[k - 1]:
    if k == i[0]:
        ar.append(i[1])
        f[i[1]] = i[2]
        pre[i[1]] = k
    else:
        ar.append(i[0])
        f[i[0]] = i[2]
        pre[i[0]] = k
while min(f.values()) == 0:
    ar2 = copy.deepcopy(ar)
    ar = []
    for j in ar2:
        for m in e[j - 1]:
                if j == m[0]:
                    if m[1] != pre[j]:
                        ar.append(m[1])
                        f[m[1]] = m[2] + f[j]
                        pre[m[1]] = j
                else:
                    if m[0] != pre[j]:
                        ar.append(m[0])
                        f[m[0]] = m[2] + f[j]
                        pre[m[0]] = j
for i in range(q):#h:高さ
    print(f[z[i][0]] + f[z[i][1]])"""




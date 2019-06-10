n = int(input())
c = []
for i in range(n - 1):#h:高さ
    c.append([int(m) - 1 for m in input().split()])
for i in range(n - 1):
    c[i].append(1)

def DFS(K, w,edges,N):
  cnt = 0
  roots=[ [] for i in range(N)]
  for a,b,c in edges:
    roots[a]+=[(b,c)]
    roots[b]+=[(a,c)]
  dist=[-1]*N
  stack=[]
  stack.append(K)
  dist[K]=0
  while stack:
    label=stack.pop(-1)
    cnt += 1
    if label != w:
        for i,c in roots[label]:
          if dist[i]==-1:
            dist[i]=dist[label]+c
            stack+=[i]
  return cnt - 1

def DFS2(K,w,edges,N):
  htg = []
  prl = []
  for i in range(n):
      """htg.append([])"""
      prl.append([])
  roots=[ [] for i in range(N)]
  for a,b,c in edges:
    roots[a]+=[(b,c)]
    roots[b]+=[(a,c)]
  dist=[-1]*N
  stack=[]
  stack.append(K)
  dist[K]=0
  """htg[0].append(0)"""
  while stack:
      label = stack.pop(-1)
      """if label != 0:
        htg[label] += htg[prl[label][0]]
        htg[label].append(label)"""
      for i,c in roots[label]:
        if dist[i]==-1:
          dist[i]=dist[label]+c
          stack+=[i]
          prl[i].append(label)
        if i==w:
            htg.append(i)
            while i != 0:
                gg = prl[i][0]
                htg.append(gg)
                i = gg
            return htg
#点は0始まり
htgn = DFS2(0, n - 1, c, n)
sroot = len(htgn) // 2
pnt = htgn[sroot - 1]

fenneccnt = DFS(0, pnt, c, n)#点は0始まり
snukecnt = n - fenneccnt
if fenneccnt > snukecnt:
    print("Fennec")
else:
    print("Snuke")
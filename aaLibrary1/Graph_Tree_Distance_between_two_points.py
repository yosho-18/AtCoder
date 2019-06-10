def DFS(K,w,edges,N):
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
    for i,c in roots[label]:
      if dist[i]==-1:
        dist[i]=dist[label]+c
        stack+=[i]
      if i==w:
        return dist[w]
root = DFS(k - 1, d, n)#点は0始まり
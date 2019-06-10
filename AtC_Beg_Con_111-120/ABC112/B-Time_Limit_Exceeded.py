n, t = map(int, input().split())

k = [list(map(int, input().split())) for i in range(n)]
"""
114514 810
931 893
364 364

c1=k[0][0] t1=k[0][1]
"""
m=[]
for i in range(n):
    if t >= k[i][1]:
        m.append(k[i][0])

m.sort()
if m != []:
    print(m[0])
else:
    print("TLE")
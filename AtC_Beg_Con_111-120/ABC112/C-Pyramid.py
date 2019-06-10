n = int(input())

w = [(list(map(int, input().split()))) for i in range(n)]#x,y,h
w.sort(key=lambda x:(x[2]),reverse=True)
hcon1 = 0
hcon2 = 0
for cx in range(101):
    for cy in range(101):
        for i in range(n):
            if w[i][2] > 0:
                if i == 0:
                    hcon1 = abs(w[i][0] - cx) + abs(w[i][1] - cy) + w[i][2]
                elif i != 0 and i != n - 1:
                    hcon2 = abs(w[i][0] - cx) + abs(w[i][1] - cy) + w[i][2]
                    if hcon1 != hcon2:
                        break
                    else:
                        hcon1 = hcon2
                else:
                    hcon2 = abs(w[i][0] - cx) + abs(w[i][1] - cy) + w[i][2]
                    if hcon1 != hcon2:
                        break
                    else:
                        print(cx,cy,hcon1)
                        exit()
            else:
                if i == 0:
                    hcon1 = 1
                elif i != 0 and i != n - 1:
                    if hcon1 > abs(w[i][0] - cx) + abs(w[i][1] - cy) + w[i][2]:
                        break
                else:
                    if hcon1 > abs(w[i][0] - cx) + abs(w[i][1] - cy) + w[i][2]:
                        break
                    else:
                        print(cx, cy, hcon1)
                        exit()






"""import numpy as np"""

"""x = np.arange(-20, 20)[:, np.newaxis, np.newaxis]
y = np.arange(-20, 20)[:, np.newaxis]
z = np.arange(-20, 20)

res = x * 411 + y * 295 + z * 161 == 3200
np.argwhere(res) - 20
print(np.argwhere(res) - 20)
"""
"""n = int(input())

k = [list(map(int, input().split())) for i in range(n)]

x = np.arange(100)[:, np.newaxis, np.newaxis]
y = np.arange(100)[:, np.newaxis]
h = np.arange(100)

res = max(0, h - abs(x - k[0][0]) - abs(y - k[0][1])) == k[0][2]
solve = list(np.argwhere(res))
print(solve)
solve2=[]
p = 0
for i in range(1, n):
    p == 0
    if i % 2 != 0:
        for s in solve:
            if max(0, s[2] - abs(s[0] - k[i][0]) - abs(s[1] - k[i][1])) == k[i][2]:
                if p == 0:
                    del solve2[:]
                    p = 1
                solve2.append(s)
    else:
        for t in solve2:
            if max(0, t[2] - abs(t[0] - k[i][0]) - abs(t[1] - k[i][1])) == k[i][2]:
                if p == 0:
                    del solve[:]
                    p = 1
                solve.append(t)

#print(np.argwhere(res))
if n % 2 == 0:
    print(solve)
else:
    print(solve2)"""
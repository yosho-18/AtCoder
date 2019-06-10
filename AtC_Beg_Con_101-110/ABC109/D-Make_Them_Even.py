h, w = map(int, input().split())
a = []
for i in range(h):#h:高さ
    a.append([int(m) for m in input().split()])
n = 0
printlist= []
for i in range(h):
    for j in range(w):
        if i % 2 == 0 and j == w - 1:
            nx = j
            ny = i + 1
            if i == h - 1:
                break
        elif i % 2 == 0 and j != w - 1:
            nx = j + 1
            ny = i
        elif i % 2 != 0 and j == w - 1:
            j = w - j - 1
            nx = j
            ny = i + 1
            if i == h - 1:
                break
        elif i % 2 != 0 and j != w - 1:
            j = w - j - 1
            nx = j - 1
            ny = i
        if a[i][j] % 2 != 0:
            a[i][j] -= 1
            a[ny][nx] += 1
            printlist.append([i + 1, j + 1, ny + 1, nx + 1])
            n += 1

print(n)
for i in range(n):
    print(printlist[i][0], printlist[i][1], printlist[i][2], printlist[i][3])

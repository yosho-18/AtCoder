h, w = map(int, input().split())
c = []
for i in range(h):#h:高さ
    c.append([str(m) for m in list(input())])
for i in range(2 * h):
    if i != 0:
        print()
    for j in range(w):
        print(c[i // 2][j], sep = "", end = "")

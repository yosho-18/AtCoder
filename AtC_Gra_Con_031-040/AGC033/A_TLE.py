
h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(str(input()))

blackli = []
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            blackli.append((i, j))

bp = len(blackli)
dd = ((0, -1), (-1, 0), (0, 1), (1, 0))
ans = 0
tmpblackli = []

while bp != h * w:
    for li in blackli:
        for dx, dy in dd:
            nx = li[1] + dx; ny = li[0] + dy
            if 0 <= nx < w and 0 <= ny < h:
                tmpblackli.append((ny, nx))
    blackli += tmpblackli
    blackli = list(set(blackli))
    ans += 1
    bp = len(blackli)
    tmpblackli = []
print(ans)
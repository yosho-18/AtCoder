import copy
H, W = map(int, input().split())
S = [input() for i in range(H)]
dd = ((-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1))
T = copy.deepcopy(S)
count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        for dx, dy in dd:
            nx = j + dx; ny = i + dy
            if 0 <= nx < W and 0 <= ny < H:
                if S[ny][nx] == '#':
                    count += 1
        T[i] = list(T[i])
        T[i][j] = str(count)
        T[i] = "".join(T[i])
        count = 0
for k in range(len(T)):
    print(T[k])


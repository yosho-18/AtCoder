from collections import deque

# 入力
H, W = map(int, input().split())
c = []
for y in range(H):
    c.append([str(m) for m in list(input())])

# startとgoalの位置を格納する
start = []
goal = []
for y in range(H):
    for x in range(W):
        if c[y][x] == "s":
            start = [y, x]
        elif c[y][x] == "g":
            goal = [y, x]

# 探索開始
flag = [[0 for x in range(W)] for y in range(H)]  # 一度訪れていたら考える必要なし
flag[start[0]][start[1]] = 1  # start地点を訪問済みにする
stack = deque()  # 訪問していく座標を格納する
stack.append(start)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while stack != deque():
    y, x = stack.pop()  # 深さ優先探索をしていく，座標を取り出す
    for dx, dy in dd:  # 4方向に動く
        nx = x + dx; ny = y + dy
        if 0 <= nx < W and 0 <= ny < H:  # 範囲内に収まっていることが必要条件
                if c[ny][nx] != "#" and flag[ny][nx] != 1:  # 塀でないかつ訪問済みでない
                    stack.append([ny, nx])
                    flag[ny][nx] = 1  # 訪問済みflagを立てる
                    if goal == [ny, nx]:  # 探索可能範囲がgoalの座標と一致していれば"Yes"を出力し，終了
                        print("Yes")
                        exit()

# 全て探索し終わって，goalまでたどり着けないと"No"を出力し，終了
print("No")
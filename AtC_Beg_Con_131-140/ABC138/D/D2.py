import sys
入力 = sys.stdin.readline
範囲, 出力 = range, print
真, 偽 = True, False
何もしない = None
一行に複数個の入力 = lambda:map(int, 入力().split())
頂点の数, 操作回数 = 一行に複数個の入力()
辺 = [[] for _ in 範囲(頂点の数)]
カウンター = [0] * 頂点の数
辺の数 = 頂点の数-1
for _ in 範囲(辺の数):
    頂点1, 頂点2 = 一行に複数個の入力()
    頂点1 -= 1
    頂点2 -= 1
    辺[頂点1] += 頂点2,
    辺[頂点2] += 頂点1,
for _ in 範囲(操作回数):
    頂点, 足す値 = 一行に複数個の入力()
    頂点 -= 1
    カウンター[頂点] += 足す値
到達済み = [偽] * 頂点の数
親 = 0
到達済み[親] = 真
スタック = [親]
while スタック:
    親 = スタック.pop()
    for 子 in 辺[親]:
        if 到達済み[子]:
            何もしない
        else:
            到達済み[子] = 真
            カウンター[子] += カウンター[親]
            スタック += 子,
出力(*カウンター)
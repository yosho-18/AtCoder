import matplotlib.pyplot as plt
import random
import numpy as np
import math
import sys

# 最小木問題をプリム法で解く

# 点群をランダム発生
p = [[random.uniform(0, 100), random.uniform(0, 100)] for i in range(100)]

# 空のリストを用意
e = []  # 部分最小木
av = []  # 部分最小木に含まれる頂点
pv = list(p)  # その他の頂点

# 始点は任意
av.append(p[0])
pv.remove(p[0])

while 1:
    # 比較のための初期値として十分大きい数を用意
    shortestlen = sys.float_info.max
    # 部分最小木に追加する辺を為す2点の初期化
    kav = None  # 部分最小木に含まれる頂点からの候補
    kpv = None  # その他の頂点からの候補
    for v1 in av:
        for v2 in pv:
            # 重みの計算（ここでは距離）
            dist = math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)
            if shortestlen > dist:
                shortestlen = dist
                # 候補の更新
                kav = v1
                kpv = v2
    if shortestlen > 0:
        # 部分最小木に追加
        e.append([kav, kpv])
    # 確定した頂点を移す
    av.append(kpv)
    pv.remove(kpv)
    # 全頂点に対する判定を終えたら終了
    if len(pv) == 0:
        break

# 最小木の描画
for l in e:
    l = np.array(l).T
    plt.plot(l[0], l[1], 'k-', lw=2)
plt.show()

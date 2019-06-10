value = [] # ノードの値を持つ配列
N = 0 # 葉の数

def update(i, x):
    # i番目の葉の値をxに変える
    i += N - 1  # i番目の葉のノード番号
    value[i] = x
    while i > 0:
        i = (i - 1) / 2  # ノード i の親ノードの番号に変える
        value[i] = min(value[i * 2 + 1], value[i * 2 + 2])  # 左右の子の min を計算しなおす


#define INF 2147483647 // 2^31-1
INF = float("INF")
def query(a, b, k, l, r) :
    # [a, b) の区間に対するクエリについて
    # ノード k （区間 [l, r) 担当）が答える
    if r <= a or b <= l:
        # 区間が被らない場合は INF を返す
        return INF
    if a <= l and r <= b:
        # ノード k の担当範囲がクエリ区間 [a, b) に完全に含まれる
        return value[k]
    else:
        # 一部だけ範囲が被る場合は左右の子に委託する
        c1 = query(a, b, 2 * k + 1, l, (l + r) / 2) # 左の子に値を聞く
        c2 = query(a, b, 2 * k + 2, (l + r) / 2, r) # 右の子に値を聞く
        # 左右の子の値の min を取る
        return min(c1, c2)




value = [] # ノードの値を持つ配列
N = 0  # 葉の数

if __name__ == '__main__':
    n = 0; q = 0 # 数列のサイズとクエリの数
    n, q = map(int, input().split())
    N = 1
    while N < n:
        N *= 2 # 葉の数を計算（n以上の最小の2冪数）

    value = vector<int>(2 * N - 1, INF)

    for j in range(q):
        c = 0
        c = int(input())
        if c == 0:
            # update(i, x)
            i = 0; x = 0
            i, x = map(int, input().split())
            update(i, x)
        else:
            # find(s, t)
            s = 0; t = 0
            s, t = map(int, input().split())
            print(query(s, t + 1, 0, 0, N))

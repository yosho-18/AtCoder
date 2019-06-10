from collections import defaultdict, deque

v, n = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(n)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    v1 = q.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)

for i in range(len(res)):
    print(res[i], ",", end="")
"""冒頭にリンクも貼った「DPの話」の記事で言われている「入次数 0 のノード (とそこから伸びる辺) をひたすら取り除きまくる」実装。

vがノードの数、nが辺の数、esが各辺を表す親ノード、小ノードのペア。

outsが各ノードから出ていく先のノードのリストの辞書。insが各ノードの入次数の辞書。

qが入次数が0のノードのキュー。

キューの頭のノードを取り出し、ソートされたリストの次のメンバとしてappend
そのノードから伸びる各辺について
その行き先のノードの入次数を１減らし
もしそのノードの入次数が0に落ちたらキューに入れる
という処理を繰り返す。

outsとinsの作成にO(E)、qの作成にO(V)、resの作成のループはO(V+E)（外側のループがO(V)回、内側のループは合計でO(E)回）ということで全体的にO(E+V)の計算量。

実際にDPでトポロジカルソートをする必要があることはあまりないらしい（入力が与えられた時点ですでにDAGとしてソートされていることが多いとのこと）。だけどとりあえず必要だったらすぐ実装して使えるようにしておきたい。今回でわかった通りロジックも実装も非常に簡単だし。"""
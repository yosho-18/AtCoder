#横にn個入力
a, b = map(int, input().split())

#n...普通、a...横で入力された複数の要素を配列で取得
n = int(input())
a = [int(m) for m in input().split()]

#d...縦で入力された複数の要素を配列で取得
n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

#行列
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])
p = []
q = []
for i in range(n):#h:高さ
    pi, qi = map(int, input().split())
    p.append(pi)
    q.append(qi)

#Grid
h, w = map(int, input().split())
c = []
for i in range(h):#h:高さ
    c.append([str(m) for m in list(input())])
#二次元リスト
w = []
for i in range(n):
    w.append([])
for i in range(n):
    for j in range(n):
        w[i].append([])
#昇順にソート、降順にソート
d.sort()
d.sort(reverse=True)
t.sort(key=lambda x:(x[0], x[1]))
aby.sort(key=ig(2), reverse=True)

#nに入った要素を一つずつ配列とする
n = input()
j = [int(x) for x in list(str(n))]

#nPn(全通り)
import itertools
for a in itertools.permutations(a):
    a = list(a)

#print(itertools.combinations_count(4, 2))
#指定の要素をリストが持つか
j[i] in ar

#forforを抜ける
else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
break  # 外側のforを抜ける

#最小のインデックス番号
t = a.index(min(a))
#リスト合計、最大
a = []
sum(a)
max(a)
"splitに区切るやつを入れる"
s=input().split('-')

arr = [[0,0], [1,1], [1,0], [1,1], [0,1], [0,0]]
arr = list(map(list, set(map(tuple, arr))))
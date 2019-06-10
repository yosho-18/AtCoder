# 全ての要素を削除
a.clear()
# 指定した位置の要素を削除し、値を取得
print(l.pop(0))
# [1, 2, 3, 5, 6, 7, 8, 9]
print(l.pop(-2))
# 8
#指定した値と同じ要素を検索し、最初の要素を削除
l = list('abcdefg')
l.remove('d')
# ['a', 'b', 'c', 'e', 'f', 'g']
#指定した所に要素を挿入する
list = ["A", "B", "C"]
list.insert(1, "D")
print list     # ["A", "D", "B", "C"]
#削除したい要素をインデックスで指定する。
l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del l[0]
del l[-1]
# [1, 2, 3, 4, 5, 6, 7, 8]
del l[2:5]
# [0, 1, 5, 6, 7, 8, 9]
del l[:3]
# [3, 4, 5, 6, 7, 8, 9]
del l[4:]
# [0, 1, 2, 3]
del l[-3:]
# [0, 1, 2, 3, 4, 5, 6]
del l[:]
# []
del l[2:8:2]#start,stop,step
print(l)
# [0, 1, 3, 5, 7, 8, 9]
del l[::3]
print(l)
# [1, 2, 4, 5, 7, 8]

#スライス
a = [1, 2, 3, 4, 5]
a[2:4:1]#[3, 4]

# 元の文字列
str = "abcdefghi"
# いったんリストにする
str_list = list(str)
print(str_list)
# リストの3番目の要素を'z'で上書き
str_list[2] = 'z'
# またリストから文字列へ戻す
str_changed = "".join(str_list)

# 元の文字列
str = "abcdefghi"
# スライスをうまいこと使う
# 「元文字列の2文字目まで」＋ 'z' + 「元文字列の4文字目以降」
str_changed = str[:2] + 'z' + str[3:]

int(input().replace(' ', ''), 2)
sum([P[j][bin(i&F[j]).count('1')] for j in range(N)])
print 11 << 1    # 22左シフト
if ((i >> b) & 1) & isopen[n][b]:

all(c in 'abcdefghijklmnopqrstuvwxyz' for c in s)
j.isupper()
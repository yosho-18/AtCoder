#d...縦で入力された複数の要素を配列で取得
n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
a = [int(m) for m in d]#int型に直す

for i in range(n):
    if i == 0:
        k = a[i]
    else:
        k = a[k - 1]
    if k == 2:
        print(i + 1)
        exit()
print(-1)
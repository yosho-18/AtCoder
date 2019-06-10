#d...縦で入力された複数の要素を配列で取得
n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
a = [int(m) for m in d]#int型に直す
a.sort()
A = sum(a)
for i in range(n):
    if A % 10 != 0:
        print(A)
        exit()
    else:
        A -= a[i]
        if i != 0:
            A += a[i - 1]
print(0)

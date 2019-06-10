#横にn個入力
h, w = map(int, input().split())
#n...普通、a...横で入力された複数の要素を配列で取得
n = int(input())
a = input().split()
a = [int(m) for m in a]
s = []
for i in range(h):
    s.append([])
v = 0
for i in range(n):
    for j in range(1, a[i] + 1):
        if len(s[v]) < w:
            s[v].append(i + 1)
        else:
            v += 1
            s[v].append(i + 1)

oore=0
for t in s:
    for i in range(len(t)):
        if oore % 2 == 0:
            print(t[i], "", end = '')
        else:
            print(t[-(i + 1)], "", end = '')
        if i == len(t) - 1:
            print()
            oore += 1
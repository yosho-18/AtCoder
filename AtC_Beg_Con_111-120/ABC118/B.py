#横にn個入力
n, m = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])

numset = set()
for i in range(1, 31):
    numset.add(i)

for i in range(n):
    numset= set(c[i][1:]) & numset
print(len(numset))
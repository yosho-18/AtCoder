n = int(input())
t = [int(m) for m in input().split()]
a = [int(m) for m in input().split()]
trcd = []
arcd = []
for i in range(n):
    if i == 0:
        trcd.append([t[i], 1])
    else:
        if t[i - 1] < t[i]:
            trcd.append([t[i], 1])
        elif t[i - 1] == t[i]:
            trcd.append([t[i], t[i]])

for i in reversed(range(n)):
    if i == n - 1:
        arcd.append([a[i], 1])
    else:
        if a[i] > a[i + 1]:
            arcd.append([a[i], 1])
        elif a[i] == a[i + 1]:
            arcd.append([a[i], a[i]])

ans = 1
mod = 10 ** 9 + 7
for i in range(n):
    if trcd[i][1] == arcd[-i-1][1] and trcd[i][1] == 1:#候補がひとつしかなくて
        if trcd[i][0] != arcd[-i-1][0]:#その候補の数字が違うとき
            print(0)
            exit()
    elif (trcd[i][0] > arcd[-i-1][0] and trcd[i][1] == 1) or (trcd[i][0] < arcd[-i-1][0] and arcd[-i-1][1] == 1):
        print(0)
        exit()
    else:
        ans *= min(trcd[i][1], arcd[-i-1][1])#候補が小さいほうをとる
        ans %= mod
print(ans)
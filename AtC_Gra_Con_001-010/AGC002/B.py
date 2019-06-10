n, m = map(int, input().split())
c = []
for i in range(m):#h:高さ
    c.append([int(m) for m in input().split()])
ball = []
for i in range(n + 1):
    if i == 1:
        ball.append([1, 1])
    else:
        ball.append([0, 1])
for i in range(m):
    if ball[c[i][0]][0] == 0:#赤ボールがないとき
        ball[c[i][0]][1] -= 1
        ball[c[i][1]][1] += 1
    elif ball[c[i][0]][1] == 1:#赤ボールがひとつ，白が0のとき
        ball[c[i][0]][1] -= 1
        ball[c[i][1]][1] += 1
        ball[c[i][1]][0] = 1
        ball[c[i][0]][0] -= 1
    else:#白がひとつ以上のとき
        ball[c[i][0]][1] -= 1
        ball[c[i][1]][1] += 1
        ball[c[i][1]][0] = 1

ans = 0
for i in range(n + 1):
    if ball[i][0] >= 1:
        ans += 1
print(ans)
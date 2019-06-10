a, b = map(int, input().split())
w = []
for i in range(100):
    w.append([])
for i in range(100):
    for j in range(100):
        w[i].append([])

for i in range(100):
    for j in range(100):
        if i < 50:
            w[i][j] = "."
        else:
            w[i][j] = "#"

acnt = 0
bcnt = 0
for i in range(0, 50, 2):
    for j in range(0, 100, 2):
        if bcnt == b - 1:
            break
        else:
            w[i][j] = "#"
            bcnt += 1
    else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
        continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
    break  # 外側のforを抜ける
for i in range(51, 100, 2):
    for j in range(0, 100, 2):
        if acnt == a - 1:
            break
        else:
            w[i][j] = "."
            acnt += 1
    else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
        continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
    break  # 外側のforを抜ける

print(100, 100)
for i in range(100):
    print(( ''.join(w[i])))

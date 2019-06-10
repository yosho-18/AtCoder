a, b = map(int, input().split())
y = []
p = 0
#w = []
for i in range(1, 1000):
    p += i
    y.append(p)
    #w.append(1)
c = b - a
for i in range(1, 999):
    if y[i] - y[i - 1] == c:
        print(y[i] - b)
        break
"""z = []
for i in range(499500):
    z.append([])
for i in range(499500):
    z[i] = list(map(lambda k: k - i - 1, y))"""
"""for x in range(1, 499501):
    for i in range(1, 999):
        if y[i] == b + x and y[i - 1] == a + x:
            print(x)
            break
    else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
        continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
    break  # 外側のforを抜ける"""

"""for h in range(1, 499501):
    y = [y1 - w1 for (y1, w1) in zip(y, w)]
    x = 100 if a > 50 else 0
    k = min(y)
    for i in range(999):
        if i != 0:
            if b == y[i] and a == y[i - 1]:
                print(h)
                break
    else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
        continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
    break  # 外側のforを抜ける"""

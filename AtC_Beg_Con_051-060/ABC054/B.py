n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
# [d1, d2, d3, ..., dN]
b = []
for i in range(m):
    b.append(input())
# [d1, d2, d3, ..., dN]
for s in range(n - m + 1):
    for t in range(n - m + 1):
        for i in range(s, m + s):
            for j in range(t, m + t):
                if a[i][j] != b[i - s][j - t]:
                    break
            else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
                if i == m + s - 1 and j == m + t - 1:
                    print("Yes")
                    exit()
                continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
            break  # 外側のforを抜ける
print("No")


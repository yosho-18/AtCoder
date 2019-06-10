h, w = map(int, input().split())
s = []

for i in range(h):
    a = input()
    s.append([str(m) for m in list(str(a))])

#print(s)
p = 0
for i in range(h):
    for j in range(w):
        if i > 0 and j > 0 and i < h - 1 and j < w - 1:
            if s[i][j] == "#" and s[i - 1][j] == s[i][j - 1] == s[i][j + 1] == s[i + 1][j] == ".":
                print("No")
                p = 1
                break
        if i == 0 and j != 0 and j != w - 1:
            if s[i][j] == "#" and s[i][j - 1] == s[i][j + 1] == s[i + 1][j] == ".":
                print("No")
                p = 1
                break
        if i == h - 1 and j != 0 and j != w - 1:
            if s[i][j] == "#" and s[i - 1][j] == s[i][j - 1] == s[i][j + 1] == ".":
                print("No")
                p = 1
                break
        if j == 0 and i != 0 and i != h - 1:
            if s[i][j] == "#" and s[i - 1][j] == s[i][j + 1] == s[i + 1][j] == ".":
                print("No")
                p = 1
                break
        if j == w - 1 and i != 0 and i != h - 1:
            if s[i][j] == "#" and s[i - 1][j] == s[i][j - 1] == s[i + 1][j] == ".":
                print("No")
                p = 1
                break
        if i == 0 and j == 0:
            if s[i][j] == "#" and s[i][j + 1] == s[i + 1][j] == ".":
                print("No")
                p = 1
                break
        if i == 0 and j == w - 1:
            if s[i][j] == "#" and s[i][j - 1] == s[i + 1][j] == ".":
                print("No")
                p = 1
                break
        if i == h - 1 and j == 0:
            if s[i][j] == "#" and s[i - 1][j] == s[i][j + 1] == ".":
                print("No")
                p = 1
                break
        if i == h - 1 and j == w - 1:
            if s[i][j] == "#" and s[i - 1][j] == s[i][j - 1] == ".":
                print("No")
                p = 1
                break

    else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
        continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
    break  # 外側のforを抜ける

if p == 0:
    print("Yes")
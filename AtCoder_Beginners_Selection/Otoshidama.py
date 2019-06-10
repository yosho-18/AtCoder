n, y = map(int, input().split())
a = n
#c = n - a - b
p = 0

for i in range(a + 1):
    b = n - i
    for j in range(b + 1):
         c = n - i - j
         #for k in range(c + 1):
         if 10000*i + 5000*j + 1000*c == y:
            print(i, j, c)
            p = 1
            break
    else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
         continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
    break  # 外側のforを抜ける

if p == 0:
    print(-1, -1, -1)
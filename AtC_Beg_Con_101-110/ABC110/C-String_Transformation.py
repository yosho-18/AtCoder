s = input()
j = [str(x) for x in list(str(s))]
t = input()
k = [str(x) for x in list(str(t))]

ar = []

for i in range(len(j)):
    if j[i] != k[i]:
        if j[i] in ar:
            break
        """if j[i] not in ar:
            ar.append(j[i])"""
        com = j[i]
        j[i] = k[i]
        if j[i] not in ar:
            ar.append(j[i])
        for h in range(len(j)):
            if j[h] == com:
                j[h] = k[i]
            elif j[h] == k[i] and h != i:
                j[h] = com
        for g in range(i + 1):
            if j[g] != k[g]:
                break
        else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
            continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
        break  # 外側のforを抜ける

if j == k:
    print("Yes")
else:
    print("No")
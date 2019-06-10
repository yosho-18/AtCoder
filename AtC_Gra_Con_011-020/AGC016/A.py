s = input()
n = len(s)
alset = set()
mojiretsu = s
chuumoku = ""
cnt = 0
ans = float("INF")
for i in range(n):
    if s[i] not in alset:
        chuumoku = s[i]
        alset.add(chuumoku)
        while len(set(mojiretsu)) != 1:
            cpmojiretsu = mojiretsu
            mojiretsu = ""
            for j in range(len(cpmojiretsu) - 1):
                if cpmojiretsu[j] == chuumoku or cpmojiretsu[j + 1] == chuumoku:
                    mojiretsu += chuumoku
                else:
                    mojiretsu += s[j]
            cnt += 1
        if ans > cnt:
            ans = cnt
        cnt = 0
        mojiretsu = s
print(ans)
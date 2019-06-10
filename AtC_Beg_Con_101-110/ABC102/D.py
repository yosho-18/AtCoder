n = int(input())
a = input().split()
a = [int(m) for m in a]
asum = []
t = 0
for i in range(n):
    t += a[i]
    asum.append(t)
x1 = 0
x2 = 0
x3 = 0
x4 = 0
s1 = 1
s2 = 3
#累積和
ansli = []
for i in range(n - 3):
    ansli.append([])
ac = 2
bc = 2
#真ん中を固定して調べていく
for i in range(2, n - 1):
    #左側の仕切りを考える（単調増加関数）
    for j in range(s1, i):
        if j == 1:#累積和の利用
            s1l = asum[0]
            s1r = asum[i - 1] - asum[0]
            cr = abs(s1l - s1r)
            ac = 2
        else:
            if ac == 1:#j == 1以外のとき増えた分を足す
                s1r += a[i - 1]
                cr = abs(s1l - s1r)
            #しゃくとり法
            s1l2 = asum[j - 1]#仕切りを動かしてどっちがいいかを調べる
            s1r2 = asum[i - 1] - asum[j - 1]
            cr2 = abs(s1l2 - s1r2)
            if cr2 <= cr:
                s1l = s1l2
                s1r = s1r2
                cr = cr2
                s1 = j
                ac = 2
            else:
                break
    ansli[i - 2].append(s1l)#iのときでもっともよい仕切り方を保存する
    ansli[i - 2].append(s1r)
    ac = 1
    # 右側の仕切りを考える（単調増加関数）
    for k in range(s2, n):
        if k == 3:
            s2l = asum[i] - asum[i - 1]
            s2r = asum[n - 1] - asum[i]
            crw = abs(s2l - s2r)
            bc = 2
        else:
            if bc == 1:
                s2l -= a[i - 1]
                crw = abs(s2l - s2r)

            s2l2 = asum[k - 1] - asum[i - 1]
            s2r2 = asum[n - 1] - asum[k - 1]
            cr2w = abs(s2l2 - s2r2)
            if cr2w <= crw:
                s2l = s2l2
                s2r = s2r2
                crw = cr2w
                s2 = k
                bc = 2
            else:
                break
    ansli[i - 2].append(s2l)
    ansli[i - 2].append(s2r)
    bc = 1
ransli = []
for i in range(n - 3):
    p = max(ansli[i])
    q = min(ansli[i])
    ransli.append(p - q)

print(min(ransli))
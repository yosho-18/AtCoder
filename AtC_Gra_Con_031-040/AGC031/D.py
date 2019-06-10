import itertools
k, n = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([str(m) for m in input().split()])

nums = [1, 2, 3]
s = ["" for _ in range(k + 1)]
flag = 1
for balls in itertools.product(nums, repeat=k):#3**k
    for i in range(n):
        if flag == 1:
            tmplen = 0
            for k1 in c[i][0]:
                tmplen += balls[int(k1) - 1]
            if tmplen == len(c[i][1]):
                j = 0
                flag = 1
                while j < len(c[i][1]):
                    if flag == 1:
                        for k_ in c[i][0]:
                            if s[int(k_)] == "":
                                s[int(k_)] = c[i][1][j:balls[int(k_) - 1] + j]
                                j += balls[int(k_) - 1]
                            else:
                                if s[int(k_)] != c[i][1][j:balls[int(k_) - 1] + j]:
                                    flag = 0
                                    for u in range(k + 1):#brakの起点はここか
                                        s[u] = ""
                                    break
                                else:
                                    j += balls[int(k_) - 1]
                    else:
                        break
            else:#ここ，初期化を忘れない
                for u in range(k + 1):
                    s[u] = ""
                break
                flag = 1
                break
        else:
            flag = 1
            break
    else:
        for i in range(1, k + 1):
            print(s[i])
        exit()
s = input()
n = int(input())

cnt = 0
for i in s:
    for j in s:
        t = i + j
        cnt += 1
        if cnt == n:
            print(t)
            exit()
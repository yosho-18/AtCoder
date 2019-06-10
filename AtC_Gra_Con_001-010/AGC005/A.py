x = input()
cnt = 0
ans = 0
for i in range(len(x)):
    if x[i] == "S":
        cnt += 1
    else:
        if cnt == 0:
            ans += 1
        else:
            cnt -= 1
print(2 * ans)
x = input()
cnt = 0
while cnt < len(x):
    if x[cnt] in ["c", "o", "k", "u"]:
        if x[cnt] == "c":
            cnt += 1
            if x[cnt] == "h":
                cnt += 1
                pass
            else:
                print("NO")
                exit()
        else:
            cnt += 1
    else:
        print("NO")
        exit()
print("YES")

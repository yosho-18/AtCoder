s = input()
t = "keyence"
p = 0
h = 0
for i in range(len(s)):
    if p == 0:
        if i <= 6:
            if s[i] == t[i]:
                h += 1
            if s[i] != t[i]:
                k = i
                p = 1
    elif p == 1:
        if s[i] == t[k]:
            j = i
            p = 2
            h += 1
        if i == len(s) - 1:
            if s[i] == "e" and k == 5:
                print("YES")
                exit()
            else:
                print("NO")
                exit()
    elif p == 2:
        if k + i - j <= 6:
            if s[i] == t[k + i - j]:
                h += 1
            elif s[i] != t[k + i - j]:
                print("NO")
                exit()
        else:
            print("NO")
            exit()
if h == 7:
    print("YES")
else:
    print("NO")
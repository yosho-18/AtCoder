s = input()
n = len(s)
mae = 0
ushiro = n - 1
ans = 0

while mae != ushiro:
    if s[mae] == s[ushiro]:
        mae += 1
        ushiro -= 1
        if mae == ushiro + 1:
            break
    elif s[mae] != s[ushiro]:
        if s[mae] == "x":
            mae += 1
            ans += 1
        elif s[ushiro] == "x":
            ushiro -= 1
            ans += 1
        else:
            print(-1)
            exit()

print(ans)
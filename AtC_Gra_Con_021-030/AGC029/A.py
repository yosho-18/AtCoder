s = input()

ans = 0
ichi = 0
for i in range(len(s)):
    if s[i] == "W":
        ans += ichi
    else:
        ichi += 1
print(ans)
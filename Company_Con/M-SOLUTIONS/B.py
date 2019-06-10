s = input()
ocnt = 0
for i in range(len(s)):
    if s[i] == "o":
        ocnt += 1

if 15 - len(s) + ocnt >= 8:
    print("YES")
else:
    print("NO")
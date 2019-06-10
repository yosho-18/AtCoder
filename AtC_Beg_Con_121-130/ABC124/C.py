s = input()
n = len(s)
ans1 = 0
for i in range(n):
    if i % 2 == 0:
        if s[i] != "0":
            ans1 += 1
    else:
        if s[i] != "1":
            ans1 += 1

ans2 = 0
for i in range(n):
    if i % 2 == 0:
        if s[i] != "1":
            ans2 += 1
    else:
        if s[i] != "0":
            ans2 += 1
print(min(ans1, ans2))
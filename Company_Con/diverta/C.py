n = int(input())
s = []
for i in range(n):
    s.append(str(input()))

Bset = set()
Aset = set()
ans = 0
for i in range(n):
    if s[i][0] == "B":
        Bset.add(i)
    if s[i][-1] == "A":
        Aset.add(i)
    for j in range(1, len(s[i])):
        if s[i][j - 1] == "A" and s[i][j] == "B":
            ans += 1

Bli = list(Bset)
Ali = list(Aset)
ans += min(len(Bli), len(Ali))
if Bset == Aset and Bset != set():
    ans -= 1
print(ans)
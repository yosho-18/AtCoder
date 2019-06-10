s = input()
t = input()
s = list(s)
t = list(t)
s.sort()
t.sort(reverse=True)

for i in range(min(len(s), len(t))):
    if s[i] < t[i]:
        print("Yes")
        exit()
    elif s[i] > t[i]:
        print("No")
        exit()

if len(s) < len(t):
    print("Yes")
else:
    print("No")

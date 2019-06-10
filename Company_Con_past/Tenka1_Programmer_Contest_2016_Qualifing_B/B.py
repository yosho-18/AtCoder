s = input()
leftcnt = 0
rightcnt = 0
ans = 0
l = s.count("(")
r = s.count(")")
#ans = abs(l - r)
for i in range(len(s)):
    if s[i] == "(":
        leftcnt += 1
    elif s[i] == ")":
        if rightcnt > 0:
            leftcnt -= 1
        else:
            rightcnt += 1

for i in range(len(s)):
    if s[i] == "(":
        leftcnt += 1
        #rightcnt -= 1 if rightcnt > 0 else 0
    elif s[i] == ")":
        if rightcnt > 0:

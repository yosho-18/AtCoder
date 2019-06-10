n = int(input())
s = input()
s = list(s)
allli = {"w":s.count("W"),"e":s.count("E")}
leftli = {"w":0,"e":0}
rightli = allli
coli = []
for i in range(n):
    if i == 0:
        if s[i] == "W":
            rightli["w"] -= 1
        else:
            rightli["e"] -= 1
        coli.append(rightli["e"])
    else:
        if s[i - 1] == "W":
            leftli["w"] += 1
        else:
            leftli["e"] += 1
        if s[i] == "W":
            rightli["w"] -= 1
        else:
            rightli["e"] -= 1
        coli.append(rightli["e"] + leftli["w"])

print(min(coli))
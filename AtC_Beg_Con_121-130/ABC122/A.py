b = input()
s = ""
for i in range(len(b)):
    if b[i] == "A":
        s += "T"
    elif b[i] == "T":
        s += "A"
    elif b[i] == "C":
        s += "G"
    else:
        s += "C"
print(s)
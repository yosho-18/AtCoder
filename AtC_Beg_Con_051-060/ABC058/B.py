o = input()
e = input()
t = ""
for i in range(len(o) + len(e)):
    if i % 2 == 0:
        t += o[i // 2]
    else:
        t += e[(i - 1) // 2]
print(t)
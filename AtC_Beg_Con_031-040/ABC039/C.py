s = input()
t = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
u = ["Do", "Do", "Re", "Re", "Mi", "Fa", "Fa", "So", "So", "La", "La", "Si"]
k = 0
for i in range(12):
    for j in range(20):
        if s[j] == t[j + i]:
            if j == 19:
                print(u[k])
                exit()
        else:
            k += 1
            break

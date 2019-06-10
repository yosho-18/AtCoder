n = input()
if len(n)==1:
    print(n)
    exit()
for i in range(1, len(n)):
    if n[i] != "9":
        print(9 * (len(n) - 1) + int(n[0]) - 1)
        exit()
print(9 * (len(n) - 1) + int(n[0]))

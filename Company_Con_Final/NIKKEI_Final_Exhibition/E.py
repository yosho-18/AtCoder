n = int(input())
tmp = ""
for i in range(1, n + 1):
    if i % 2 == 0:
       tmp += "a"
    if i % 3 == 0:
        tmp += "b"
    if i % 4 == 0:
        tmp += "c"
    if i % 5 == 0:
        tmp += "d"
    if i % 6 == 0:
        tmp += "e"
    print(tmp if tmp != "" else i)
    tmp = ""
sa = input()
sb = input()
sc = input()
if sa[0] == "a":
    k = "a"
    sa = sa[1:]
elif sa[0] == "b":
    k = "b"
    sa = sa[1:]
elif sa[0] == "c":
    k = "c"
    sa = sa[1:]
while True:
    if k == "a":
        if sa != "":
            k = sa[0]
            sa = sa[1:]
        else:
            print("A")
            exit()
    elif k == "b":
        if sb != "":
            k = sb[0]
            sb = sb[1:]
        else:
            print("B")
            exit()
    elif k == "c":
        if sc != "":
            k = sc[0]
            sc = sc[1:]
        else:
            print("C")
            exit()
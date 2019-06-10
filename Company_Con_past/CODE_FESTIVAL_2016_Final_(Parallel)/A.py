h, w = map(int, input().split())
c = []
for i in range(h):#h:高さ
    c.append([str(m) for m in input().split()])
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(h):
    for j in range(w):
        if c[i][j] == "snuke":
            print(ALPHA[j],i + 1,sep="")

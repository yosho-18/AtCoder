n, d, k = map(int, input().split())
lr = []
for i in range(d):#h:高さ
    lr.append([int(m) for m in input().split()])
st = []
for i in range(k):#h:高さ
    st.append([int(m) for m in input().split()])

for i in range(k):
    stmp = st[i][0]
    ttmp = st[i][0]
    for j in range(d):
        if lr[j][0] <= stmp <= lr[j][1]:
            stmp = lr[j][0]
        if lr[j][0] <= ttmp <= lr[j][1]:
            ttmp = lr[j][1]
        if stmp <= st[i][1] <= ttmp:
            print(j + 1)
            break

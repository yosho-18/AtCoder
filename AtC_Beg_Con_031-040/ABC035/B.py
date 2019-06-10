import collections
s = input()
t = int(input())
xt1 = 0
yt1 = 0
xt2 = 0
yt2 = 0
c = collections.Counter(s)
#c = collections.defaultdict(int)
xt1 += abs(c["L"] - c["R"]) + c["?"]
yt1 += abs(c["U"] - c["D"])

xt2 += abs(c["L"] - c["R"])
wwxt2 = xt2
yt2 += abs(c["U"] - c["D"])

qq = xt2 - c["?"]
if qq >= 0:
    xt2 -= c["?"]
else:
    xt2 = 0
    rr = yt2 - (c["?"] - wwxt2)
    if rr >= 0:
        yt2 = abs(yt2 - (c["?"] - wwxt2))
    else:
        if (-rr) % 2 == 1:
            yt2 = 1
        else:
            yt2 = 0

if t == 1:
    print(xt1 + yt1)
else:
    print(xt2 + yt2)


n = int(input())
if n==1:
    print("Hello World")
else:
    d = []
    for i in range(2):
        d.append(input())
    # [d1, d2, d3, ..., dN]
    d = [int(m) for m in d]
    print(d[0]+d[1])
    """print("tsevfsevb")
    s = [1, 2]
    print(s)
    s.clear()
    print(s)"""
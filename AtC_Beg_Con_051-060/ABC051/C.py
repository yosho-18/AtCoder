sx, sy, tx, ty = map(int, input().split())
nsx, nsy = sx, sy
while nsy < ty:
    nsy += 1
    print("U", end = "")
while nsx <= tx:
    nsx += 1
    print("R", end = "")
while nsy >= sy:
    nsy -= 1
    print("D", end="")
while nsx > sx:
    nsx -= 1
    print("L", end = "")
nsy += 1
print("U", end = "")
nsx -= 1
print("L", end = "")
while nsy <= ty:
    nsy += 1
    print("U", end = "")
while nsx < tx:
    nsx += 1
    print("R", end = "")
while nsy > sy:
    nsy -= 1
    print("D", end="")
while nsx > sx:
    nsx -= 1
    print("L", end = "")


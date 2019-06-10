n, a = map(int, input().split())
k = int(input())
b = [int(m) for m in input().split()]

circle = []
circleset = set()
start = 0
counter = 0
while True:
    a = b[a - 1]
    counter += 1
    if k == counter:
        print(a)
        exit()
    if a in circleset:
        for val in range(len(circle)):
            if circle[val] == a:
                start = val
                break
        break
    else:
        circle.append(a)
        circleset.add(a)

loop = k - start
loopli = circle[start:]
mod = len(loopli)
place = loop % mod
print(loopli[place - 1])
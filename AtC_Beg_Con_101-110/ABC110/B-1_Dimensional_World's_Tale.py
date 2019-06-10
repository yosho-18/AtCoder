n,m,x,y = map(int, input().split())
n = int(n)
m = int(m)
x = int(x)
y = int(y)
s = []
for i in range(2):
    a = input().split()
    s.append([int(m) for m in a])

s[0].append(x)
s[1].append(y)
p = max(s[0])
q = min(s[1])

if p >= q:
    print("War")
else:
    print("No War")
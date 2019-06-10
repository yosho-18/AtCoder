n = int(input())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])
count = 0
for j in range(n):
    count += s[j][1] - s[j][0] + 1
print(count)
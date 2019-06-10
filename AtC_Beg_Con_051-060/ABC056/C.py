x = int(input())
t = 0
j = 0
for i in range(1, x + 1):
    t += i
    if t >= x:
        j = i
        break
print(j)
"""i = 1
count = 0
while True:
    if i == 1:
        t = x
    s = t - i
    if s == 0:
        break
    elif s >= i + 1:
        t = s
    else:
        t = s + i
    i += 1

print(i)"""
a,b,c = map(int, input().split())
ar = [a,b,c]
ar.sort()
t = ar[2]#max
u = ar[1]
v = ar[0]#min
tu = t - u
tv = t - v
count = 0
if tu % 2 == 0 and tv % 2 == 0:
  count += tu
  count += int((tv - tu) / 2)
elif tu % 2 != 0 and tv % 2 != 0:
  count += tu
  count += int((tv - tu) / 2)
else:
  count += tu
  count += int((tv - tu - 1) / 2) + 2

print(count)

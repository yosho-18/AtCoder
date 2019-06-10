n= input()
t = list(n)
t = [int(i) for i in t]
s = 0
for j in t:
  s += j

if int(n) % s == 0:
  print("Yes")
else:
  print("No")

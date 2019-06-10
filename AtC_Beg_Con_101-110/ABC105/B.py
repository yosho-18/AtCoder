n = int(input())
p = 0
for i in range(26):
  for j in range(16):
    if 4*i + 7*j == n:
      p = 1
      break
if p == 0:
  print("No")
else:
  print("Yes")

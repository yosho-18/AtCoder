name = input()
n = len(name)
for i in range(n):
  if name[i] != name[-i - 1]:
    print("NO")
    break
else:
  print("YES")

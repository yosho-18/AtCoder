x = int(input())

ar = []

for i in range(2, 11):
  for j in range(1, 40):
    if j ** i <= x:
      ar.append(j ** i)
print(max(ar))

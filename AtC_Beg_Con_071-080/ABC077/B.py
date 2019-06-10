import math as m
n = int(input())
for i in range(n,-1,-1):
  if m.sqrt(i) == int(m.sqrt(i)):
    print(i)
    exit()
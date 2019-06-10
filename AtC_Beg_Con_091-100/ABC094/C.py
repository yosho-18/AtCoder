import copy
import statistics
n = int(input())
x = [int(y) for y in input().split()]
z = copy.deepcopy(x)
z.sort()
t = (z[int(n / 2) - 1] + z[int(n / 2)]) / 2

for i in range(n):
  if x[i] < t:
    print(z[int(n / 2)])
  else:
    print(z[int(n / 2) - 1])
"""import copy
n = int(input())
x = [int(y) for y in input().split()]
z = copy.deepcopy(x)

for i in range(n):
  x.pop(i)
  x.sort()
  print(x[int((n - 1) / 2)])
  del x[:]
  x.extend(z)

 
  import copy
n = int(input())
x = [int(y) for y in input().split()]
z = copy.deepcopy(x)

for i in range(n):
  x.pop(i)
  x.sort()
  print(x[int((n - 1) / 2)])
  del x[:]
  x.extend(z)


import copy
n = int(input())
x = [int(y) for y in input().split()]
z = copy.deepcopy(x)

p = [copy.deepcopy(x) for i in range(n)]
  
for i in range(n):
  p[i].pop(i)
  p[i].sort()
  print(p[i][int((n - 1) / 2)])


import copy
n = int(input())
x = [int(y) for y in input().split()]
z = copy.deepcopy(x)
for i in range(n):
  x.pop(i)
  x.sort()
  print(x[int((n - 1) / 2)])
  del x[:] 
  for j in z:
    x.append(j)

"""
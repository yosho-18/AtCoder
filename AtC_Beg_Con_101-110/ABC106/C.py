s = input()
k = int(input())

s = list(s)

co = 1

for i in s:
    if int(i) == 1:
        if co == k:
            print(int(i))
            break
    else:
        print(int(i))
        break
    co += 1


"""s = input()
k = int(input())
 
s = list(s)
v = 5 * 10**15
a = []
for i in range(9):
  a.append(i ** v)

nuar = []
lear = []
co = 0
rear = 0

for i in s:
  for j in range(1,10):
    if int(i) == j:
      nuar.append(j)
      rear += a[j - 1]
      lear.append(rear)
      
for p in range(len(s)):
  if p == 0:
    if lear[p] >= k:
      print(nuar[p])
  elif lear[p] >= k and lear[p - 1] < k:
    print(nuar[p])
  
 
"""
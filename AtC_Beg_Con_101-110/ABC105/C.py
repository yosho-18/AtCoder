n = int(input())
li = []
res = n % (-2)
ans = n // (-2)
ans1 = n
if res != 0:
    res = ans1 - (-2) * (ans + 1)
    ans = ans + 1
ans1 = ans
li.append(res)
p = 0
if ans == 0 or ans == 1:
    p = 1
    if ans == 1:
      li.append(ans)
while p == 0:
  res = ans % (-2)
  ans = ans // (-2)
  if res != 0:
      res = ans1 - (-2) * (ans + 1)
      ans = ans + 1
  ans1 = ans
  li.append(res)
  if ans == 0 or ans == 1:
    p = 1
    if ans == 1:
      li.append(ans)
li = [str(n) for n in li]
pr = ""
for i in range(len(li)):
  pr += li[-1-i]
print(pr)

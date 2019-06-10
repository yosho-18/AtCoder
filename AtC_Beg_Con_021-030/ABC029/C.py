import itertools
n = int(input())
alphali = ["a", "b", "c"]
ans = ""
for balls in itertools.product(alphali, repeat=n):#3**n
  for i in balls:
  	ans += i
  print(ans)
  ans = ""

s = input()
t = ""
count = 0
for i in range(len(s)):
  if i == 0:
    t += s[i]
  elif i == len(s) - 1:
    t += s[i]
  else:
    count += 1
    if i == len(s) - 2:
      t += str(count)
print(t)

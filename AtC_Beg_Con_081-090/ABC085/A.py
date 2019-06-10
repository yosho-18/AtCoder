s = input()
c = ""
for i in range(len(s)):
  if i != 3:
    c += s[i]
  else:
    c += "8"

print(c)

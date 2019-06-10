s = input()
if "E" in s and "W" in s and "N" in s and "S" in s:
  print("Yes")
elif "E" in s and "W" in s and "N" not in s and "S" not in s:
  print("Yes")
elif "E" not in s and "W" not in s and "N" in s and "S" in s:
  print("Yes")
else:
  print("No")

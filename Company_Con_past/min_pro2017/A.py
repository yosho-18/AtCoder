s = input()
k = (s.count("y") == 1) and (s.count("a") == 1) and (s.count("h") == 1) and (s.count("o") == 2)
print("YES" if k else "NO")
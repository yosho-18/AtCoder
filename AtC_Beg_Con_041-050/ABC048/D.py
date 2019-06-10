s = input()
n = len(s)
if (n % 2 == 0 and s[0] == s[-1]) or (n % 2 != 0 and s[0] != s[-1]):
    print("First")
else:
    print("Second")
s1, s2, s3 = map(str, input().split())
alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t1 = ALPHA[alpha.index(s1[0])]
t2 = ALPHA[alpha.index(s2[0])]
t3 = ALPHA[alpha.index(s3[0])]
print(t1 + t2 + t3)
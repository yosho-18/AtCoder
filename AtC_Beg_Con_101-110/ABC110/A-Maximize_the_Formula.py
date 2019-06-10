a,b,c = map(int, input().split())
i = int(str(a)+str(b))+c
i2= int(str(b)+str(a))+c
j = int(str(b)+str(c))+a
j2= int(str(c)+str(b))+a
k = int(str(c)+str(a))+b
k2= int(str(a)+str(c))+b
n = max(i,i2,j,j2,k,k2)
print(n)

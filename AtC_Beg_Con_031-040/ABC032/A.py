a = int(input())
b = int(input())
n = int(input())
i = n
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        #print()
        exit()
    i += 1
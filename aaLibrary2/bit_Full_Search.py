#A = [0, 1, 2, 3]の部分集合を全て出力する
A = [0, 1, 2, 3]

for i in range(1 << len(A)):
    output = []
    for j in range(len(A)):
        if ((i >> j) & 1) == 1:
            output.append(A[j])
    print(output)
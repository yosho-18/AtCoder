x = [1, 8, 14, 23, 44, 55, 67, 88, 103, 146]
print(x)
#""探したい数字を入力"
i = int(input())

low = 0
high = len(x)
# t は中央番目の数
t = (low + high) // 2

# 探索の下限のlowが上限のhighになるまで探索
# lowがhighに達すると数は見つからなかったということ
while (low<=high):
    if (i==x[t]):
        break
    elif (i > x[t]):
        low = t + 1
    elif (i < x[t]):
        high = t - 1
    t = (low + high) // 2

if (i==x[t]):
    print(str(t + 1) + "番目にあります")
else:
    print("ありません")
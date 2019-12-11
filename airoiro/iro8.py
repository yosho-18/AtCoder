# 値からindex番号を取得
if nums[i] != nums[P]:
    return [copy_nums.index(nums[i]), copy_nums.index(nums[P])]  # 被りなし，被っていたら一番最初のもの，無いものはエラー
else:
    ans = [i for i, x in enumerate(copy_nums) if x == nums[i]]  # 被りあり，全て取り出す
    return ans[:2]

# 無いものに対応
def my_index2(l, x, default=False):
    return l.index(x) if x in l else default

print(my_index2(l, 'd'))
# 3

print(my_index2(l, 'x'))
# False

print(my_index2(l, 'x', -1))
# -1
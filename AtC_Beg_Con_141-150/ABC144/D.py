import torch
k = [5, 2, 0, 1, 4]
s = torch.tensor([1423, 35, 567, 678, 234, 654, 7567, 23])
#p = s[k]

x = torch.tensor([5, 2, 0, 1, 4])
p = s[x]
print(p)
print(x ** 3)
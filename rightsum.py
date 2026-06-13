nums = [10,4,8,3]
n = len(nums)
l = []
l1 = []
l2 = []
sum_r = 0
sum_l = 0
l.append(sum_r)
l1.append(sum_l)
for r in range(n - 1, 0, -1):
    sum_r = sum_r + nums[r]
    l.append(sum_r)
    l2 = l[::-1]
print(l2)
for left in range(0,n-1,1):
    sum_l = sum_l + nums[left]
    l1.append(sum_l)
print(l1)
result = list(set(l1)-set(l2))
print(result)
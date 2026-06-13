nums = [10,4,8,3]
left_sum = []
right_sum = []
l = []
sum_l = 0
sum_r = 0
n= len(nums)
left_sum.append(sum_l)
right_sum.append(sum_r)
for i in range(0,n-1):
    sum_l+=nums[i]
    left_sum.append(sum_l)
for i in range(n-1,0,-1):
    sum_r+=nums[i]
    right_sum.append(sum_r)
    right_sum.sort(reverse=True)
for i in range(n):
    answer = left_sum[i]-right_sum[i]
    l.append(abs(answer))
print(l)






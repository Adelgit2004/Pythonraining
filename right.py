nums = [1,2,3,4,5,6,7]
k = int(input())
l = []
l1 = []
l3 = []
for i in range(k+1, len(nums) , 1):
    l.append(nums[i])
    l.sort()
print(l)
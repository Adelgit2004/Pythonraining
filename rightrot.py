nums = list(map(int,input().split()))
k = int(input())
l=[]
nums.sort(reverse = True)
for i in range(0,k):
    l.append(nums[i])
    l.sort()
print(l)
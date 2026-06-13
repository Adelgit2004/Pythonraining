list1 = list(map(int,input().split()))
k = int(input())
s = sum(list1[:k])
m = s
for i in range(1,len(list1)-k+1):
    s = s-list1[i-1]+list1[i+k-1]
    m = max(m,s)
print(m)




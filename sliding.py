list2 = list(map(int,input().split()))
k = int(input())
m = 0
for i in range(0,len(list2)-k+1):
    sum=0
    for j in range(i,i+k):
        sum += list2[j]
        m = min(m,sum)
print(m)





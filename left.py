l = list(map(int,input().split()))
k = int(input())
n = len(l)
for i in range(0,k):
    first = l[0]
    for j in range(0,len(l)-1):
        l[j] = l[j+1]
    l[n-1] = first
print(l)

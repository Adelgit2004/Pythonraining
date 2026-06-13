list1 = [2,1,6,2,1,2,4,7,8,1,2]
r,m,s,l = 0,0,0,0
k = 10
while(s<len(list1)-1):
    s+=list1[r]
    while(s>k):
        s -= list1[l]
        l+=1
    length = r-l+1
    m = max(m,length)
    r+=1
print(m)




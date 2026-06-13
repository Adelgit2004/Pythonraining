l1=[1,2,3,5]
l2 = [5,6,7,8]
l3= []
n = len(l1)
m = len(l2)
i,j,k = 0,0,0
while(i<n and j<m):
    if(l1[i]<l2[j]):
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
while(i<n):
    l3.append(l1[i])
    i += 1
while(j<m):
    l3.append(l2[j])
    j += 1
print(l3)


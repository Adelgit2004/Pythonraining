def countsteps(k,c):
    if k==1:
        return c
    elif(k%2==0):
        c+=1
        return countsteps(k/2,c)
    elif(k%4==3):
        c+=1
        return countsteps(k+1,c)
    else:
        c+=1
        return countsteps(k-1,c)
print(countsteps(15,0))
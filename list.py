li = [2,3,4,5,6,7,8,9]
l2 = []
li.sort()
for i in li:
    if(i%2!=0):
        l2.append(i)
    else:
        l2.insert(0,i)
print(l2)


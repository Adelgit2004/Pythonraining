n = list(map(int,input().split()))
r = len(n)
l = []

for i in range(0,(len(n)//2)):
    l.append(n[i])
    l1 = l[::-1]
for j in range(len(n)//2,len(n)):
    l.append(n[j])
    l2 = l[r//2:]
l3 = l1 + l2
print(l3)


# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting
arr = list(map(int,input().split()))
k = int(input())
n = len(arr)
l = []
l1 = []
for i in range(k-1,-1,-1):
    l.append(arr[i])
    l.sort()
for j in range(len(arr)-1,k-1,-1):
    l1.append(arr[j])
l2 = list(reversed(l1))
l3 = l2+l
print(l3)





aliceSizes = [1,1],
bobSizes = [2,2]
for i in range(1, len(aliceSizes)):
    for j in range(0, 1):
        aliceSizes[i] = bobSizes[j] + aliceSizes[i-1]
print(temp)
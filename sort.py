names = ["Mary","John","Emma"],
height = [180,165,170]
l = []
height.sort()
n = len(names) == len(height)
for i in range(0, n):
    if (names[i] == height[i]):
        height.sort()
        l.append(names[i])
print(names)

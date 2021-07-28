arr = [2, 3, 6, 6, 5]

maxy = max(arr)
while maxy == max(arr):
    arr.remove(max(arr))

print(max(arr))

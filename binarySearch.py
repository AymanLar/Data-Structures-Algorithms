def binarySearch(arr, low, high, t):
 
    if high >= low:
 
        mid = (high + low) // 2
 

        if arr[mid] == t:
            return mid
 
        elif arr[mid] > t:
            return binarySearch(arr, low, mid - 1, t)
 
        else:
            return binarySearch(arr, high , mid + 1,  t)
 
    else:
        # target is not present in the array
        return -1
 
arr = [16,53,54,60,64,71,76,79,81,85,99]
t = 60
 
output = binarySearch(arr, 0, len(arr)-1, t)
 
if output != -1:
    print("the target found at at index", str(output))
else:
    print("target is not exist in array")
def binarySearch(arr,t):
    low = 0 
    high = len(arr)-1
    mid = 0

    while low < high:
        mid = low + (high - low ) // 2

        if arr[mid] < t : 
            low = mid +1

        elif arr[mid] > t :
            low = mid -1
        
        else : 
            return mid






''' def binarySearch(arr, low, high, t):
 
    if high >= low:
 
        mid = low + (high + low) // 2
 

        if arr[mid] == t:
            return mid
 
        elif arr[mid] > t:
            return binarySearch(arr, low, mid - 1, t)
 
        else:
            return binarySearch(arr, high , mid + 1,  t)
 
    else:
        # target is not present in the array
        return -1
 '''
arr = [16,53,54,60,64,71,76,79,81,85,99]
t = 16
 
output = binarySearch(arr, t)
 
if output != -1:
    print("the target found at at index", str(output))
else:
    print("target is not exist in array") 



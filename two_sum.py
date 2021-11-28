target=18 
arr= [2,7,11,15]

def sum(arr,target):
    for i in range(len(arr)):
        if arr[i]+arr[i+1] == target:
            return i , i+1

print(sum(arr, target))
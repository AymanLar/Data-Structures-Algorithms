def bubbleSort(arr):

    lenght = len(arr)

    for i in range(lenght-1):
        for j in range(lenght-i-1):
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j] # index swapping


arr = [100,64,23,18,48,94,23,30,98,94]

bubbleSort(arr)

print('sorted array is : ')
print(arr)
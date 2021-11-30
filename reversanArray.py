def reverseArr(arr,s ,e ):
    # s = 0  start of arr 
    # e = n-1  end of arr 
    while s < e :
        arr[s], arr[e] = arr[e] , arr[s]
        s +=1
        e -= 1

arr = [7, 9, 0, 4, 2]
print(arr)
reverseArr(arr, 0, 4)
print("Reversed list is")
print(arr)
print(reverse(arr))
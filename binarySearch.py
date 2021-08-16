def binarysearch(array , target):
    first = array[0]
    last = len(array) - 1

    while last > first :
        mid = (first + last) // 2

        if array[mid] == target:
            return mid 

        elif target > array[mid]:
            first =  mid +1

        else target < array[mid]:
            last  =  mid -1 

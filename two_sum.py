def twoSum(array, target):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            
            if array[i] + array[j] == target:
                return ([array[i], array[j]])

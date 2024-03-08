def mergeSort(arr):
    # we split the array if it has more than one element
    if len(arr) > 1: 
        mid = len(arr) // 2
        leftArray = arr[:mid]
        rightArray = arr[mid:]
        print(f'left array = {leftArray}, right array = {rightArray}')
        mergeSort(leftArray)
        mergeSort(rightArray)
    
    
        # merge step
        i = 0 
        j = 0 
        k = 0 # used to overwrite the array but this time in a sorted order
        while i < len(leftArray) and j < len(rightArray): 
            if leftArray[i] <= rightArray[j]: 
                arr[k] = leftArray[i]
                i += 1 
            else: 
                arr[k] = rightArray[j]
                j += 1 
            k += 1
        
        if i < len(leftArray): 
            arr[k:] = leftArray[i:]
        elif j < len(rightArray): 
            arr[k:] = rightArray[j:]
        return arr
    
array = [18, 12, 11, 10, 5, 1, 2, 6, 7]
print(f'original array = {array}')
print(mergeSort(array))

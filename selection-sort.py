# For every passthrough we select the smallest element and put it where...
# ... we began the passthrough
def selectionSort(arr):
    smallestElementIndex = 0
    beginPassThrough = 0 # [5, 3, 1, 7, 8]
    for i in range(len(arr)):
        for j in range(beginPassThrough, len(arr)): 
            if arr[j] < arr[smallestElementIndex]:
                smallestElementIndex = j 
        arr[beginPassThrough], arr[smallestElementIndex] = arr[smallestElementIndex], arr[beginPassThrough]
        beginPassThrough += 1
        smallestElementIndex = beginPassThrough
    return arr

print(selectionSort([5, 4, 3, 2, 1]))
print(selectionSort([5, 3, 1, 7, 8]))

# Reference: Jay Wengrow chapter 4, page 51
# NOTE: after every passthrough we are guaranteed to have an element it's correct position
# For instance when we are sorting in ascending order after the first passthrough...
# ...the largest element ends up at the end of the list.
# For the next passthrough the next largest element ends up next to the largest and so on.
# That's why we have a the 'sortUntil' variable to show where we have to sort up to.
# Because beyond that point the elements are already sorted ( [..., nextlargest, largest] )

def bubbleSort(arr):
    sorted = False
    sortUntil = len(arr) - 1
    while not sorted: 
        sorted = True
        for i in range(sortUntil): 
            if arr[i] > arr[i + 1]: 
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(arr) # See that after every passthrough the an element will be in the correct position. 
        # This movement of elements towards the end of the array looks like a bubbling effect hence the name of the algorithm
        sortUntil -= 1 
    return arr

bubbleSort([1, 2, 4, 6, 7, 8, 1])
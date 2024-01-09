# Reference: Jay Wengrow chapter 6, page 76
# PRODEDURE: We pick an element (We start at index 1) and compare ... 
# every other element left to that element. 
# If an element is greater than the target element we shift it one index up
# Otherwise we place the target element in front of it (To achieve an ascending order)
# More visualization in the reference

def insertion_sort(arr):# [4, 2, 7, 1, 3]
    for start_index in range(1, len(arr)): 
        compare_index = start_index - 1 
        current_value = arr[start_index]
        while compare_index > - 1 and arr[compare_index] > current_value:
            arr[compare_index + 1] = arr[compare_index]
            compare_index -= 1 
        arr[compare_index + 1] = current_value
    return arr 

# Wengrow implementation
def insertion_sort_2(array):
    for index in range(1, len(array)):
        position = index
        temp_value = array[index]
        while position > 0 and array[position - 1] > temp_value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = temp_value
    return array

def insertion_sort_3(arr): 
    for start_index in range(1, len(arr)): 
        current_value = arr[start_index]
        for compare_index in range(start_index - 1, -2, -1): 
            if compare_index > - 1 and arr[compare_index] > current_value: 
                arr[compare_index + 1] = arr[compare_index]
            else: 
                # We perform this operation whenever the any of above condition fails
                
                # The first condition will only be false (when compare_index = -1) When we have ...
                # compared all elements to the left of the 'current_value' and all of them are greater...
                # than the 'current_value'
                # In other words the 'current_value' is smaller than every element to it's left
                
                # The second condition will be false if any element at index 0 or above (Since the first condition must be true first)...
                # is less than the 'current_value'
                
                # So whichever one is false we need to perform the operation below
                arr[compare_index + 1] = current_value
                break 
            
    return arr 


print(insertion_sort_3([4, 2, 7,1, 1, 1, 0, 0, 0, -1, 1, 3]))
                
    
# RULES:
# an array is a directory []
# files are the elements of an array [1, 1, 1, 1, ..., 1]
# an array inside another array is a subdirectory [1, 1, .., [ 1, 1, ..., 1], 1, 1, 1]
# So the task is to combine all these into a single directory
# In other words flatten the array

def combine_directories(arr):
    def inner(arr, index, result:list):
        # This is the base case 
        # If the index is out of bounds then we must be at the end
        # So we return the result we have
        if index == len(arr): 
            return result
        
        # If we encounter a subdirectory we first have to put all its ...
        # ... elements inside the general directory
        # We call the function again but this time the directory in question will ...
        # ... be the subdirectory.
        # We start at index 0 for that subdirectory but we pass the general directory as an ...
        # ... argument so that we keep on adding new files to it
        
        if isinstance(arr[index], list): 
            inner(arr[index], 0, result)
        else: 
            result.append(arr[index])
            # This is the main step where we add a file to the general directory
        return inner(arr, index + 1, result) # we call the function again but with the next index (index + 1)
    return inner(arr, 0, []) # we initiate the process when this function is called and return the result
            
    


print(combine_directories([1, 2, 2, [1, 2, [2, 2, 2, [6, 6, 7]]]]))
    
# Reference: Jay Wengrow chapter 10, page 124 

# Partitioning 
# To partition an array means selecting a random value from the array ... 
# ... which is then called the pivot and making sure that all values less ... 
# ... than the pivot come before it and all values greater than the pivot come after it

# We are creating a class which has a partition and quicksort method
class SortableArray: 
    def __init__(self, arr): 
        self.arr = arr
        
    def partition(self, start_index, end_index):
        left = start_index
        pivot_index = end_index
        pivot = self.arr[pivot_index]
        right = pivot_index -  1
        while True:
            # break when value is greater than pivot
            while self.arr[left] < pivot: 
                left += 1
                
                # NOTE: left pointer can never go out of bounds because ... 
                # ... for instance if every other element is less than the pivot ... 
                # ... The left pointer will eventually land on the pivot itself which ... 
                # ... is not less than itself (example [1, 1, 1, 1, 1, 2])
                # You will notice that the right pointer will not move because it ... 
                # ... is already pointing to an element less than the pivot
                # So according to our code the pivot will just stay intact
                
                
            # break when value is less than pivot
            while self.arr[right] > pivot: 
                right -= 1 
                # NOTE: right pointer can never go out of bounds because ...
                # ... this is python and -1 as an index of a list is possible 
                # For instance if every other element is greater than the pivot the right ... 
                # ... pointer will continue to decrement but when it gets to -1, self.arr[-1] ... 
                # ... refers to the pivot itself which cannot be greater than itself
                # The left pointer will never move so we swap the first element with the pivot causing ... 
                # The pivot to come before all other elements (eg. [5, 5, 5, 5, 5, 2])
            
            if left >= right: 
                break
            elif self.arr[left] == self.arr[right]: 
                # This was an edge case where both left and right elements ... 
                # ... were equal to the pivot so none of the pointers increments ... 
                # ... consequently resulting an infinite loop (swapping doesn't make any difference)
                # Example [0, 2, 1, 3, 1, 2, 2]
                # So I just increment the left pointer to continue the process
                left += 1 
            else:
                self.swap(left, right)
        self.swap(left, pivot_index)      
        return left
    
    def swap(self, index_a, index_b):
        self.arr[index_a], self.arr[index_b] = self.arr[index_b], self.arr[index_a]
         
    def quicksort(self, left, right):

        # base case is if we have one or no elements
        if right <= left:
            return 
        
        pivot_index = self.partition(left, right)
        
        self.quicksort(left, pivot_index - 1)        
        self.quicksort(pivot_index + 1, right)
    
    def __str__(self):
        arr = [str(i) for i in self.arr]
        return f"[{', '.join(arr)}]"
        
arr = [0, 5, 2, 4, 5, 1, 2, 9, 0, 2, 1, 6, 3]
# arr = [5, 5, 5, 5, 5, 2]
sortable_arr = SortableArray(arr)
sortable_arr.quicksort(0, len(arr) - 1)
print(sortable_arr)
        
        

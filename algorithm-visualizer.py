arr = [1, 4, 5, 10, 1, 4, 5, 6, 7, 12, 12, 18, 1, 3, 3, 5, 15, 9, 8, 7, 6, 3, 2]

# This version of the function will not work properly for duplicates
def visualRep(heights: list):
    heightsCopy = heights.copy()
    heightsCopy.sort()
    rowCount = max(heights)
    colCount = len(heights)
    index = 0 # index of current minimum height
    excludedPositions = []
    strings = []
    currentMinHeight = heightsCopy[index]
    strings.append('#' * colCount)
    excludedPositions.append(heights.index(currentMinHeight))
     
    for i in range(1, rowCount): 
        result = ''
        currentHeight = i + 1 
        for j in range(colCount):
            if j == excludedPositions[-1] and currentHeight > currentMinHeight: 
                result += ' '
                index += 1
                currentMinHeight = heightsCopy[index]
            elif j in excludedPositions and j != excludedPositions[-1]:
                result += ' '
            else: 
                result += '#'
        strings.append(result)
        newPosition = heights.index(currentMinHeight)
        if excludedPositions[-1] != newPosition: # just to avoid redundant appends
            excludedPositions.append(newPosition)
    
    
    for i in range(len(strings) - 1, -1, -1): 
        print(strings[i])
def getIndeces(value, array):
    return [i for i, j in enumerate(array) if j == value]
# This is the complete version of the function that works even for duplicates
def visualRepComplete(heights: list):
    heightsCopy = heights.copy()
    heightsCopy.sort()
    rowCount = max(heights)
    colCount = len(heights)
    index = 0 # index of current minimum height
    excludedPositions = []
    strings = []
    indexRecords = {}
    currentMinHeight = heightsCopy[index]
    previousMinHeight = currentMinHeight
    strings.append('#' * colCount)
    newPositions = getIndeces(currentMinHeight, heights)
    excludedPositions.extend(newPositions)
     
    for i in range(1, rowCount): 
        result = ''
        currentHeight = i + 1 
        for j in range(colCount):
            if j in excludedPositions[-len(newPositions):] and currentHeight > currentMinHeight: 
                result += ' '
            elif j in excludedPositions and j not in excludedPositions[-len(newPositions): ]:
                result += ' '
            else:
                result += '#'
            
        if currentHeight > currentMinHeight: 
            while currentMinHeight == previousMinHeight:
                index += 1
                currentMinHeight = heightsCopy[index]
            previousMinHeight = currentMinHeight
            newPositions = getIndeces(currentMinHeight, heights)
            excludedPositions.extend(newPositions)
            
        strings.append(result)
        
    for i in range(len(strings) -1, -1, -1): 
        print(strings[i])


def bubbleSort(arr):
    sorted = False
    sortUntil = len(arr) - 1
    while not sorted: 
        sorted = True
        for i in range(sortUntil): 
            if arr[i] > arr[i + 1]: 
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        visualRep(arr)
        print()
        sortUntil -= 1 
    return arr



def insertion_sort_2(array):
    for index in range(1, len(array)):
        position = index
        temp_value = array[index]
        while position > 0 and array[position - 1] > temp_value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = temp_value
        visualRepComplete(array)
        print()
    return array

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
        visualRep(arr)
        print()
    return arr

# the sorts have different profiles 

# bubbleSort(arr)
insertion_sort_2(arr)
# selectionSort(arr)
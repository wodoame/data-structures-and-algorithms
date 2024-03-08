import random
arr = [11, 10, 1,1, 4, 1, 1,1, 1, 1, 1] 
random.shuffle(arr)

def getIndeces(value, array):
    return [i for i, j in enumerate(array) if j == value]

   
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
        visualRepComplete(arr)
        print()
        sortUntil -= 1 
    return arr

visualRepComplete(arr)
print()
bubbleSort(arr)

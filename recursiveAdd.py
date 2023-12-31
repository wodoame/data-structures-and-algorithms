# a function that adds all digits of a number continuously until we get a number greater than 9 

def recursiveAdd(num, calls):
    if num < 10: 
        return [num, calls]
    num = str(num) 
    digitSum = 0
    for digit in num:
        digitSum += int(digit)
    return recursiveAdd(digitSum, calls + 1)
        
print(recursiveAdd(12432463456873456, 1))
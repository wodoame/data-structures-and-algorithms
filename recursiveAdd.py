# a function that adds all digits of a number continuously until we get a single digit
# This uses the concept of recursion

def recursiveAdd(num):
    if num < 10: 
        return num
    num = str(num) 
    digitSum = 0
    for digit in num:
        digitSum += int(digit)
    return recursiveAdd(digitSum)
        
print(recursiveAdd(12432463456873456))
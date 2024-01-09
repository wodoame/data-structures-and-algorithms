# Reference: Jay Wengrow chapter 8, page 104 

# A stack is basically an array with the following restrictions: 
# Data can only be inserted, read or removed from the end of the array 
# Read the reference for more information

class Stack: 
    def __init__(self, arr=[]):
        self.stack = arr
    
    def read(self):
        return self.stack[-1]
    
    def insert(self, value):
        self.stack.append(value)
        
    def remove(self): 
        self.stack.pop()
    
    def __str__(self):
        stack = [str(i) for i in self.stack]
        return f"[{', '.join(stack)}]"
    
    def length(self):
        return len(self.stack)
    
    def isEmpty(self): 
        return len(self.stack) == 0
  
            
stack = Stack()

# I'm using the stack object to determine if a string has the correct syntax (linter)
def lint(str):
    open_brackets = {'(', '[', '{'}
    close_brackets = {'}': '{', ']': '[', ')':'('}
    for char in str: 
        if char in open_brackets:
            stack.insert(char)
        elif close_brackets.get(char): 
            if stack.read() == close_brackets.get(char):
                stack.remove()
            else: 
                return 'unmatching bracket'
    if stack.isEmpty(): 
        return 'No errors encountered'
    else: 
        return 'unclosed bracket'

print(lint('const func = () => {};'))
print(lint('const func = () => {;'))
print(lint('const func = () => {];'))
print(lint('const func = (] => {];'))

            
            
    



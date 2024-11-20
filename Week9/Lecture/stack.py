from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, newValue):
        self.stack.append(newValue)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Stack is empty")
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Stack is empty")
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def printStack(self):
        print(self.stack)


def checkExpressionDeque(exp):
    match = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    stack = deque()
    for ch in exp:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            topCh = stack[-1]
            if match[ch] == topCh:
                stack.pop()
            else:
                return False
    
    return not stack


def checkExpression(exp):
    match = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    stack = Stack()
    for ch in exp:
        if ch in "({[":
            stack.push(ch)
        else:
            if stack.isEmpty():
                return False
            topCh = stack.peek()
            if match[ch] == topCh:
                stack.pop()
            else:
                return False
    
    return stack.isEmpty()
        

# main
s = "([])(((((((((((((())))))))))))))"
print(checkExpressionDeque(s))
"""
myStack = Stack()
print(myStack.isEmpty())
myStack.push(10)
myStack.push(20)
myStack.push(30)
val = myStack.pop()
print(val)
myStack.printStack()
print(myStack.isEmpty())
val = myStack.peek()
print(val)
myStack.printStack()
"""
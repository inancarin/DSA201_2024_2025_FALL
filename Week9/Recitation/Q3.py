from collections import deque

def Evaluate_Reverse_Polish_Notation(expression):
    stack = deque()
    expression = expression.split(" ")
    
    for val in expression:
        if val in "+-*/":
            val2 = stack.pop()
            val1 = stack.pop()
            if val == "+":
                temp = val1 + val2
            elif val == "-":
                temp = val1 - val2
            elif val == "*":
                temp = val1 * val2
            elif val == "/":
                temp = val1 // val2
            stack.append(temp)
        else:
            stack.append(int(val))
    
    return stack[-1]


# main
exp = "10 6 9 3 + -11 * / * 17 + 5 +"
res = Evaluate_Reverse_Polish_Notation(exp)
print(res)
from collections import deque

def simulate_undo(commands):
    stack = deque()
    for elem in commands:
        if elem != "UNDO":
            stack.append(elem)
        elif stack and elem == "UNDO":
            stack.pop()
    return stack

# main
myCommands = ["UNDO", "insert", "UNDO"]
res = simulate_undo(myCommands)
print(res)
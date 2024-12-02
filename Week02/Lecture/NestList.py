def recursiveCount(myList):
    cnt = 0
    for elem in myList:
        if not isinstance(elem, list):
            cnt += 1
        else:
            cnt += recursiveCount(elem) # recursive part
    return cnt

# main
names = ["Adam", ["Bob", ["Chet","Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
res = recursiveCount(names)
print(res)

myList = [10, 20, 30] # lists are mutable
myList[1] = 40

s = "Ataturk" # strings are immutable
s[2] = "o"
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    maxVal = -1
    for k in keyboards:
        for d in drives:
            if k + d <= b and k + d > maxVal:
                maxVal = k + d
    return maxVal

res = getMoneySpent([40, 50, 60], [5, 8, 12], 60)
print(res)
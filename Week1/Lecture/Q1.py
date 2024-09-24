def findTheMostCommon(myList):
    d = {}
    for elem in myList:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1
    
    maxValue = max(d.values())
    allResults = []
    for k, v in d.items():
        if v == maxValue:
            allResults.append(k)
    
    return min(allResults)

res = findTheMostCommon([1,1,2,2,3])
print(res)
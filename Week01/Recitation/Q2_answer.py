import math

def checkAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    d1 = {}
    for ch in s1:
        if ch in d1:
            d1[ch] += 1
        else:
            d1[ch] = 1
    
    d2 = {}
    for ch in s2:
        if ch in d2:
            d2[ch] += 1
        else:
            d2[ch] = 1
    
    if len(d1) != len(d2):
        return False

    for k,v in d1.items():
        if k not in d2 or d1[k] != d2[k]:
            return False
    return True

def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s)):
        temp = {}
        for idx in range(0, len(s)-i+1):
            subs = s[idx:idx+i]
            check = False
            for k in temp.keys():
                if checkAnagram(subs, k):
                    check = True
                    temp[k] += 1
            if not check:
                temp[subs] = 1
        for k,v in temp.items():
            if v > 1:
                count += math.comb(v,2)
    return count

print(sherlockAndAnagrams("cdcd"))
    

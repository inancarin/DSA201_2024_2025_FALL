s = input("Enter an input: ")

d = {} # an empty dictioary
# d = dict()

for ch in s:
    if ch.isalpha():
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

maxVal = max(d.values())

for k, v in d.items():
    if v == maxVal:
        print(k, maxVal)
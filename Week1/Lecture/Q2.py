def isPangram(s):
    s = s.lower()
    d = {}
    for ch in s:
        if ch.isalpha():
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
    if len(d) == 26:
        return "pangram"
    else:
        return "not pangram"

# main
res = isPangram("We promptly judged antique ivory buckles for the next prize")
print(res)
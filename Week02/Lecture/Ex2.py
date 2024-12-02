s = input("Enter a string: ")

d = set() # create an empty set

for ch in s:
    if ch.isalpha():
        d.add(ch)

res = len(d)
print(res)
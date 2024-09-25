import math

"""
val = math.sqrt(18)
val_floor = math.floor(val)
val_ceil = math.ceil(val)
print(val)
print(val_floor)
print(val_ceil)
"""

def encrypt(s):
    # remove spaces
    s = s.replace(" ", "")
    L = len(s)
    row = math.floor(math.sqrt(L))
    col = math.ceil(math.sqrt(L))
    if row * col < L:
        row += 1
    
    mat = []
    for i in range(row):
        temp = []
        for j in range(col):
            if i * col + j < L:
                temp.append(s[i * col + j])
            else:
                temp.append("")
        mat.append(temp)
    
    res = ""
    for j in range(len(mat[0])):
        for i in range(len(mat)):
            res += mat[i][j]
        res += " "
    return res 

ans = encrypt("have a nice day")
print(ans)
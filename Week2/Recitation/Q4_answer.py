def superDigit(n, k):
    # Write your code here
    n = n * k
    if len(n) == 1:
        return int(n)
    total = 0
    for elem in n:
        total += int(elem)
    return superDigit(str(total), 1)

print(superDigit("148", 3))
def factorial(n):
    if n == 1:
        return 1 # base case
    
    return n * factorial(n-1) # recursion part

def factorial2(n):
    print("Calling the function with n value", n)
    if n == 1:
        print("Function returns 1")
        return 1 # base case
    res = n * factorial2(n-1) # recursion part
    print("Returning function with", res)
    return res

def factorial_without_recursion(n):
    res = 1
    for i in range(2, n+1) : # 2*3*4*...*n
        res *= i # res = res * i
    return res

ans = factorial2(4)
ans = factorial_without_recursion(4)
print(ans)
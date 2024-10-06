import time

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

start = time.time()
res = fibonacci_recursive(40)
print(res)
end = time.time()
print("Recursive version takes", end-start, "second(s).")

start = time.time()
res = fibonacci_iterative(40)
print(res)
end = time.time()
print("Iterative version takes", end-start, "second(s).")
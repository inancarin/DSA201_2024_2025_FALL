import Factorial
import time, math

start = time.time()
for i in range(1000000):
    res = Factorial.factorial(100)
end = time.time()
print("This operation for recursion is", end-start, "second(s).")

start = time.time()
for i in range(1000000):
    res = Factorial.factorial_without_recursion(100)
end = time.time()
print("This operation for iterative is", end-start, "second(s).")

start = time.time()
for i in range(1000000):
    res = math.factorial(100)
end = time.time()
print("This operation for math module is", end-start, "second(s).")
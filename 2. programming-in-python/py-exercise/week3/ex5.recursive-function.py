from math import factorial


#find factorial by for loop
def find_factorial_by_looping(n):
    if n < 0:
        return
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

print(find_factorial_by_looping(5))
print("--------------------------------------------->")
#factorial by recursive function
def find_factorial_by_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_by_recursive(n-1)

print(find_factorial_by_recursive(6))
n = int(input())
def fib(n): # computes the fibonacci value of nth number in the series
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
        return(f)
    
print('fibonacci of n is:',fib(n))

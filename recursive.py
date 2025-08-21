## fibbonacci series 
# 0 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6  7  8


def fib(n):
    if n == 0 or n == 1 :
        return n
    return fib(n-2 ) + fib(n-1)

print(fib(3))
 

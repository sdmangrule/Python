def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

var = int(input("Enter a number : "))

# print first 10 numbers
for i in range(var):
    print(fib(i), end=' ')

#print ("Enter a number :")
#var = int(input("Enter a number : "))
print()

# Iterative Version (Best in real world)
def fib1(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(10):
    print(fib1(i), end=" ")
#finding the Fibonacci Sequence f = f(n-1) + f(n-2)
# 0 1 1 2 3 5 8 13
x = int(input("enter a number to find fib"))
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2, n):
        c = a +b
        a = b
        b = c
        print("\n",c)

fib(x)
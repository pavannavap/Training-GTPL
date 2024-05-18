# finding the factorial of the number formula n! = n*n-1
#5!= 5*4*3*2*1 = 120

# by creating the fact function

def fact(n):

    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

x=int(input("enter a number to find factorial:- "))
resu = fact(x)

print(resu)
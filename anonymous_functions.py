# if we create a function without name it's called as anonymous funtion or lambda's.
from functools import reduce
f = lambda a : a*a
result = f(5)

print(result)
#-----------------------------------------
d = lambda a,b : a+b
result = d(5,6)

print(result)

#==========================================================================================================
# using lamdas in filter, map, reduce
# def is_even(a):
#     return a%2 == 0

nums = [3,2,4,6,5,7,8,2]
#evens = list(filter(is_even,nums))

evens = list(filter(lambda n: n%2==0,nums))
print(evens)

#=================
# mapp the data and update using lambda
def upda(a):

    return a+2

doubles1 = list(map(upda, evens))
print("printing with def")
print(doubles1)

doubles= list(map(lambda n : n+2 , evens))

print("print with lambda",doubles)

#douing reduce the list

def add_all(a,b): # using def function
    return a+b

sum = reduce(add_all,doubles)

print(sum)

#using lambda function

sum1 = reduce(lambda a,b : a+b, doubles)
print(sum1)
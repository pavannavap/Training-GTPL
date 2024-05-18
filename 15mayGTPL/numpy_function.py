from numpy import *

# the ways of creation of array
#array
arr = array([1,2,3,4,5],int)
print(arr)

print(arr)
#linspace
arr1 = linspace(0,15,16)
print(arr1)

#arrage
ar = arange(0,15,2)
print(ar)

#zeros
arr2 = zeros(15)
print(arr2)

#ones
arr3 = ones(15)
print(arr3)

# copy array from excisting array

arr4 = array([1,2,3,4,5])


# adding two array's
a = array([1,2,3,4,5])
b = array([3,6,2,7,9])
c = a+b
print(c)

#mathamatic operations on array

arr5 = array([4,3,7,5,3,5])
arr6 = array([1,2,3,4,5])

print(min(arr5))
print(sqrt(arr5))
print(max(arr5))
print(concatenate([arr5,arr6]))

# array copy

arr5 = array([4,3,7,5,3,5])
arr6 = arr5.conj()

print(arr6)


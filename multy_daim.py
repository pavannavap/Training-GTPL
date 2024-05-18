from numpy import *

arr = array([[1,2,3,4],[2,3,4,5]])
print(arr.dtype)

print( arr.ndim)

print(arr.shape)

print(arr.size)

# to convert two to one daimentional

arr1 = arr.flatten()
print(arr1)

# printing metrix
m = matrix(arr)
print(m)

# metrixs

m1 = matrix('1 2 3; 6 5 4; 2 3 5')
m2 = matrix('6 4 3; 7 4 2; 7 4 2')

m3 = m1 + m2
print(m3)

m4 = m1 * m2

print("multiplication")
print(m4)
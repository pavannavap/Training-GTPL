#Array are similar as a list but we have to store only same data type of data
# we don't have array's directly like set, tuple we have to import.
from array import *

values = array('i',[5,4,5,6,78])
print(values)

#for checking size of array for the we have built in functions

print(values.buffer_info())
# (2435944061232, 5)
#    this address, size


# to print array reverse
values.reverse()
print(values)

# to print one letter in array
i = 0
for i in values:
    print(i)

# while loopa in array
print('===================')
i = 0
while i<len(values):
    print(values[i])
    i+=1


# create an array to get the values from an user
arr = array('i',[])
n = int(input("Enter the length:- "))
for i in range(n):
    x = int(input("Enter next value:- "))
    arr.append(x)

print(arr)

# search the user entered value in array

val = int(input("enter the value:- "))

k = 0
for i in arr:
    if i == val:
        print(k)
        break
    k +=1

# we can use function for knowing the index value

print(arr.index(val))
#printing the list of values in function

# trying to finding even and odd numbers count
list = [20,40,33,56,76,45,8,944,90]

def count(int):
     even = 0
     odd = 0

     for i in list:
         if i % 2 == 1:
             even += 1
         else:
             odd += 1
     return even, odd

even, odd = count(list)
print(even)
print(odd)
print("even: {} and odd: {} ".format(even,odd))
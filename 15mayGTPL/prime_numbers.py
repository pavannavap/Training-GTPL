# to find a prime number
num = int(input("enter a number to check it is prime number or not :- "))

for i in range(2,num):
    if num % i == 0:
        print("not prime number")
        break
else:
    print("Given number is prime number")
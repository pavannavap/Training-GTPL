#we have two types of loopings i.e while and for loops

# while loop works with based on condition and it will use when we want to print
# a statement before the condition
x = 1

while x <= 5:
    print("Good")
    x = x + 1

# nested while

x = 1

while x <= 5:
    print("Hello ", end="")
    y = 1
    while y <= 4:
        print("world ", end="")
        y = y + 1
    x = x+1
    print(" ")


# for loop
#==================
# for loop will print a continues formate of a list or string

x = ['naven','pavan','kumar','44.56',2.5]

for i in x:
    print(i)

# using range with gap between 10 and 50
for i in range(10,50,5):
    print(i)

# if condition in side of for loop

for i in range(30):
    if i%2 == 0:
        print(i)



# for else looping

num = [12,23,34,45,56,67,78,89,90]

for nums in num:

    if nums % 5 == 0:
        print(nums)
        break
else:
    print("not found")
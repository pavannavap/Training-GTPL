x = int(input("Howmany candy's you want"))

# if we want to print no of candy's
i = 1
while i <=x:
    print("candy")
    i+=1

# if we want to prtint count of prints with Break condition
avg = 10

x = int(input("Howmany candy's you want"))
i = 1
while i <=x:
    if i>=avg:
        print("we are out of stock")
        break
    print("candy")
    i+=1

print("Bye")


# continues statement
i = 1
for i in range(1,50):
    if i%2==1:
        continue
    print(i)
    i+=1


# pass function
# pass is used to skip a block or function witch one we don't want to use

i = 1
for i in range(1,50):
    if i%2==1:
        pass
    i+=1
print("end")
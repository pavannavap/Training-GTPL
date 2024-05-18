# # file handaling is the concept to handle the files
# # for read the file
# f = open('MyData','r')
 
# print(f.read())     # to print entaire file data
# print(f.readline(), end="") # to print line by line

# """
# for Write some thing in to the file
# if we dont have that file witch we mentioned in that then it's create the file with that name 
# """
# f1 = open('Demo_Data','w')
# f1.write('I am The Intern in GTPL')

# print(f1.readline())

# # here i am appending the data in to the file
# f2 = open('MyData','a')
# f2.write('the text wrote by pavan')

# print(f2.readline())

# to copy the data from one file to another file
# f3 = open('MyData','r')
# f4 = open('Demo_Data','w')

# for data in f3:
#     f4.write(data)
#     print("done")

# f5 = open('Demo_Data','r')
# print(f5.read())

# if i deals with pics

# f6 = open('Pavan.jpeg','rb')
# f7 = open('My_pic.jpeg','wb')

# for data in f6:
#     f7.write(data)
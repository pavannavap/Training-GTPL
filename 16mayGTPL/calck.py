def add():
    print("result 1")

def sub():
    print("result 2")

def main():
    sub()
    add()
# here i am adding a function to call when i run clack function stand alone
# when i run the special_variable file it's print only add function in calck not call main function
# if i run calck then it's print and call main function and print all the functions

if __name__ == "__main__":
    main()


# # Exception hadaling

# a = 10
# b = 0

# try:
#     print("Program stared")
#     print(a/b)

#     k = int(input("Enter a number"))
#     print(k)

# except ZeroDivisionError as e:
#     print("You can't devided a number with zero :-" , e)

# except ValueError as e:
#     print("Invalid input:- ", e)

# except Exception as e:
#     print("something is wrong")

# finally:
#     print("Program closed")



# Multy threading
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class World(Thread):
    def run(self):
        for i in range(5):
            print("World")
            sleep(1)

t1 = Hello()
sleep(0.2)
t2 = World()

t1.start()
t2.start()


t1.join()
t2.join()
print("Bye")

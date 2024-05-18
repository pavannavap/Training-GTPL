"""
-> abstract class :- witch class is having abstract methods that class is called abstract class
-> abstract method :- witch method have delcaration but dont have any defination of that method that method is called abstract method
"""

from abc import ABC, abstractmethod
class Computer(ABC): # ABC class

    @abstractmethod  # ABC method
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print("It's Running")


class TV(Computer):
    def process(self):
        print("It's Showing")

class Desctop(Computer):
    def process(self):
        print("It's Creating")

#=======================================================================
## here i am used iterators to iterate the numbers from 0 to 10
    def __init__(self):
        self.num =1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num+=1

            return val
        else:
            raise StopIteration
        
# here i am using Generators 
# if we don't want to use iterators then that time we go for the generators

    # def maths():
    #     n = 1

    #     while n <= 10:
    #         sq = n*n
    #         yield sq
    #         n += 1

    # val = maths()

    # for i in val:
    #     print(i)


## iterators
values = Desctop()

print(next(values))

for i in values:
    print(i)

# res1 = Laptop()
# res2 = TV()
# res3 = Desctop()
# res1.process()
# res2.process()
# res3.process()
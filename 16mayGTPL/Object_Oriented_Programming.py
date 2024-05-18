"""
->OOPs object oriented programming
->object dealing based on two things 1-atribute 2-behaviour
->atribute nothing but a details of object like hight,wait
->behaviour nothing what they are doing

->class:- class is nothing but a blue print of the object
"""


#class:-
class Computer:

    def config(self):
        print("Window")

comp1 = Computer()# here comp1, comp2 are the ojects
comp2 = Computer()

Computer.config(comp1)# here i am calling the method using class directly
Computer.config(comp2)

# most of the case we use this
comp1.config()
comp2.config()



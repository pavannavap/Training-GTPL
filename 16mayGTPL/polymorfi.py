# polymorphism
# it's nothing but doing a task ina no of forms or no possibles
# types of polymorphism
"""
-> Duck type
-> Operator Overloading
-> Method Overloading
-> Method Overriding
"""

# Ducktype
# it runs the code with based on passing ide not about class or object names

class Pycharm:

    def execute(self):
        print("Compailed")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Compailing")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = Pycharm()

lap1 = Laptop()
lap1.code(ide)


#Operator Overloading
# passing the different orguments to the operator it's called operator overloading

# Python Program illustrate how
# to overload an binary + operator
# And how it actually works

class A:
	def __init__(self, a):
		self.a = a

	# adding two objects
	def __add__(self, o):
		return self.a + o.a


ob1 = A(6.8)
ob2 = A(2)
ob3 = A("Hello")
ob4 = A("World!")

print(ob1 + ob2)
#print(ob3 + ob4)
# Actual working when Binary Operator is used.
# print(A.__add__(ob1 , ob2))
# print(A.__add__(ob3,ob4))
# #And can also be Understand as :
# print(ob1.__add__(ob2))
# print(ob3.__add__(ob4))



#method overloading and method overriding

class Addit:
    def add(self, a=None, b=None, c=None):
        r = 0

        if a is not None and b is not None and c is not None:
            r = a + b + c
        elif a is not None and b is not None:
            r = a + b
        else:
            r = a
        return r

a1 = Addit()
print(a1.add(2, 8, 10))
print(a1.add(2, 8))



# method overriding

class Dog():

    def sound(self):
        print("Bow")

class Cow(Dog):

    def sound(self):
        print("MMMMMM")

c = Cow()
d = Dog()

c.sound()
d.sound()




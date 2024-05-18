# Inheritance is the ability of one class to inherit another class. Inheritance provides reusability of code and allows us to create complex and real-world-like relationships among objects.
# single inheritance
class Main():

    def __init__(self):
        print("It's and __init__ of superclass(Main)")

    def demo(self):
        print("class1 of method1")

    def demo1(self):
        print("class1 of method2")

class Subclass(Main):

    def demo2(self):
        print("class2 of method1")

    def demo3(self):
        print("class2 of method2")

s1 = Subclass()

s1.demo()
s1.demo1()
s1.demo2()
s1.demo3()
#=======================================================================
# multy level inheritance
print("Multilevel")

class Sub2(Subclass):

    def demo4(self):
        print("class3 of method2")


su1 = Sub2()

su1.demo()
su1.demo1()
su1.demo2()
su1.demo3()
su1.demo4()
#================================================================================
#multiple inheritance is two parent classes and one sub class
# here i am inherit the main class and C class hase to inherit in to the D class

print("Multiple level")
class C():

    def __init__(self):
        print("It's and __init__ of superclass(c)")

    def demo5(self):
        print("class4 of method2")

class D(Main,C):

    def demo6(self):
        print("class5 of method2")



d1 = D()
d1.demo()
d1.demo1()
d1.demo5()
d1.demo6()


#===============================================================================
#  Constructor in Inheritance
# created a init in super class and sub class

class Cons(Main):

    def __init__(self):
        super().__init__()
        print("It's and __init__ of subclass")

    def demo7(self):
        print("class6 of method2")

con = Cons()


#method resolution order
#it's count from left to right
print("==============multiple __init__")
class Cons1(Main,C):

    def __init__(self):
        super().__init__()
        print("It's and __init__ of subclass(cons1)")

    def demo7(self):
        print("class6 of method2")

r = Cons1()



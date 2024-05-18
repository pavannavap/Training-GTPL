class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.Laptop = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.Laptop.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand,self.ram,self.cpu)

s1 = Student('pavan',2)
s1 = Student('kumar',4)

s1.show()

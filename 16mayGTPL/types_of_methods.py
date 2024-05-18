# methods
# instant method, class method and static method
# instant ->accessor methods
       #  -> Mutator Method

class Student:

    school = "JNTU"

    def __init__(self, m1, m2, m3):
        self.m2 = m2
        self.m3 = m3
        self.m1 = m1

    def avg(self): # instant method
        return (self.m3 + self.m1 + self.m2)/3

    @classmethod
    def getschool(self):
        return self.school

    @staticmethod
    def info():
        print("this is static")

s1 = Student(34,45,56)
s2 = Student(56,45,34)

print(s1.getschool())
print(s1.avg())
Student.info()
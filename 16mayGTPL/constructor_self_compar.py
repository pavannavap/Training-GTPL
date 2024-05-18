# constructor
# self
class computer:

    def __init__(self):
        self.name = "pavan"
        self.age = 26

    def update(self):
        self.age=30

    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = computer()
c1.age = 30
c2 = computer()

if c1.compare(c2):
    print("they are same")
else:
    print("They are not same")

print(c1.age)
print(c2.age)


# variables
# instance , static variable
# instant variable:-
# static variables:-

class car:

    wheels = 4  # class variables or static variable

    def __init__(self):
        self.mil = 10      #
        self.com = 'BMW'    # instant variables

c1 = car()
c2 = car()

c1.mil = 23

car.wheels = 8

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
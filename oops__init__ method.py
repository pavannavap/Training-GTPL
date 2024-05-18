class Computer:

    def __init__(self,name,city): # act like as a constructor and here assigned the variables
        self.name = name
        self.city = city

    def config(self):
        print(self.name, ' from ',self.city)

comp1 = Computer('pavan','mpl')# here comp1, comp2 are the ojects
comp2 = Computer('raju','bgl')


comp1.config()
comp2.config()
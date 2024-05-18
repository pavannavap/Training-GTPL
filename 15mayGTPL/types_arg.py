# types of arguments

# normal form arg
def person(name,age):
    print(name)
    print(age)

person('pavan', 26)
person(26, 'pavan')

# keyword arg
def person(name,age):
    print(name)
    print(age)

person(name='pavan', age= 26)

#Default arg
def person(name,age = 26):
    print(name)
    print(age)

person('pavan')

#passing multiple values
def sum(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)

sum(5,4,3,4,5)

# don't mentioned starting number
def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)

sum(5,4,3,4,5)





#======================================
# variable length arg

def person(name, *data):
    print(name)
    print(data)


person('pavan', 26, 'Bgl', 6392694738)

# keyword variable arg
def person(name, **data):
    print(name)
    print(data)


person('pavan', age=26, city='Bgl', phno=6392694738)

# printing value along with key

def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)

person('pavan', age=26, city='Bgl', phno=6392694738)

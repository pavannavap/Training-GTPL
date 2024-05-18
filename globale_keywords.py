# scope of the function is either in out side of the function and inside of the function

a = 10 #== Globale variable
def something():
    a = 20 # local variable
    print(a)

something()

print(a)

# making the local variable into globale

a = 10 #== Globale variable
def something():
    global a
    a = 20 # local variable
    print(a)

something()

print(a)

# we can't use globale and local variables at a function at a time so we use a function call globalse
a = 10 #== Globale variable
def something():
    a = 20 # local variable
    x = globals()['a']
    print(a)
    print(x)

something()

#print(a)
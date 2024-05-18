# when we want to change or do some extra modifications to the function on that time we will use this decorators
def div(a, b):
    # if a<b:
    #     a,b = b,a   # in this case this dev function i dont have acces to chage this case we go for decorators
    print (a/b)

div(2,4)

# adding decorators to the function
def smart_dev(function):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return function(a,b)
    return inner

div = smart_dev(div)

div(2,4)
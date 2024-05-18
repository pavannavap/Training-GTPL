# creation and calling the function

def great():
    print("Hello!")


great()


# doing calculations
def add(x, y):
    a = x + y
    return a


print(add(10, 20))


def mul(x, y):
    result = x * y
    return result


print(mul(10, 20))

print(mul(2, 5))


# to print two functions

def add_sub(x, y):
    r = x + y
    s = x - y
    return r, s


result1, result2 = add_sub(4, 5)
print(result1, result2)

from calck import add

def fun1():
    add()
    print("from fun1")

def fun2():
    print("from fun2")

def mai():
    fun2()
    fun1()

mai()
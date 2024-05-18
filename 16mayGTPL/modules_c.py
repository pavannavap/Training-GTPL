# to reduce the bugs in big project for that break it small parts it's called modules
# if we do any changes in one module it's won't affect another one

from calc import *

a = 10
b = 20

c = sum(a, b)
print(c)

d = mul(a, b)
print(d)

e = div(a, b)
print(e)

f = sub(a, b)
print(f)

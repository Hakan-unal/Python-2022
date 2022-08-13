import module



print(module.number)
print(module.numbers)
print(module.obj)
print(module.summary(10,20))


import module as m



print(m.number)
print(m.numbers)
print(m.obj)
print(m.summary(10,20))

from module import number

print(number)

from module import numbers,obj

print(numbers)
print(obj)


from module import *




print(summary(20,30))

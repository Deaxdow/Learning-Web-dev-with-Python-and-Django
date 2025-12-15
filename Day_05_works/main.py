"""
def custmfunc():
    x = 34
    y = 56

    print(x+y)

custmfunc()
"""

#Genral Parameter Example
"""
def parafunc(x,y):
    print(x+y)

parafunc(56,89)
parafunc(78,87)
parafunc(65,-56)

"""

#Required and Optional Parameter Example
"""
def parafun2(x,y,z=0,n=100,m=2):  

#Setting default values
#Default value always have to set from back
#For this case I setted default values from 'm' then 'n' then 'z'

    print(x+y+z+m+n)
                                
parafun2(45,67,89,76) 
parafun2(67.53,23,12,45)    
parafun2(5,4,5)
"""

#Tuple parameter / Length parameter : creates tuple
"""
def parafun3(*x):
    print(x)

parafun3()
parafun3(23)
parafun3(23,45,66)
parafun3(45,23,12,45,67)    
"""

#Keyword Parameter
"""
def parafun4(**x):
    print(x)

parafun4(name="Dexadow",age="21")
"""

#Single return function
"""def funcrtr():
    name="Ali"
    age=23
    state=["NYC"]


    return name


print(funcrtr())
"""

#Multiple return function
"""
def funcrtr():
    name="Ali"
    age=23
    state=["NYC"]


    return name


print(funcrtr())
"""


#Local variable Examples
"""
def custmfunca():
    x = 34
    y = 56

    print(x+y)


def custmfuncb():
    x = 5
    y = 6

    print(x+y)


def custmfuncc():
    x = 23
    y = 12

    print(x+y)


custmfunca()
custmfuncb()
custmfuncc()    
"""

#Global variable
"""
z=123
def custmfunca():
    x = 34
    y = 56

    print(x+y+z)


def custmfuncb():
    x = 5
    y = 6

    print(x+y+z)


def custmfuncc():
    x = 23
    y = 12

    print(x+y+z)


custmfunca()
custmfuncb()
custmfuncc()   
"""

#Lamda function example
"""
result = lambda x,y : x+y
print(result(4,5))
"""

#Recursive function example
"""
def factorial(x):
    if x == 0 :
        return 1
    
    return x * factorial(x-1)

print(factorial(5))    
"""

#Call back function example

def add(x,y):
    return x+y

def result(a):
    print(a)

result(add(4,5))    


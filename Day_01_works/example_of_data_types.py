# Numerals Data types ->
"""
x=67
y=41.67
print(x+y)
"""


# string data types ->
""" 

title = "Hello,I'm learning python"
subtitle = "Python day-01"
                                   
print(title)
print(subtitle)

#if a string is contained in single quote on both side
singleQstring = 'Hello,I'm learning python'

#if a string is contained in double quote on both side
doubleQstring = "Hello,I'm learning python"

#if a string is contained in triple single quote on both side
tripleSQstring = '''Hello,I'm learning python'''

#if a string is contained in triple double quote on both side
tripleDQstring = (double quote)""Hello,I'm learning python ""(double quote)                  
            
            # can't give triple double quote on both side idk it shows error when quoted, works fine when its running  

"""


# sequence (lists) #lists contains 3rd bracket []
"""

countries = ["China","Russia","France"]
        #0 ->1 ->2 ->3 

marks=[12,14,15,16] #0 ->1 ->2 ->3 
temp =[33.4,32.4,9] #0 ->1 ->2 ->3 

                                                                  
print(countries)
print(marks)
print(temp)

"""


# sequence(tuple) , tuple is kinda list  #tuple contains 1st bracket
"""
countries = ("China","Russia","France")
            #0 ->1 ->2 ->3 
 
marks=(12,14,15,16) #0 ->1 ->2 ->3 ->4
                                                        
temp =(33.4,32.4,9) #0 ->1 ->2 ->3 ->4
"""


# Mapping
"""

}

person={
    "firstName":"Alex",
    "lastName":"Balor",
    "age":32,
    "gender":"Male",
    "isAmerican":True,
    "wealth":1318917489743424324324242,
    "color":"white",
    "height": "6 ft"
}

"""

# Sets (random sequence)
"""
names={"Ali","Einstein","Newton","Denis"}
print(names)
"""

# Boolean(True,False)
"""

 isActive=True, #true=1
 
 isActive=False, #false=0

"""


# Null data type
"""
mobileNumber= (none) ,
"""



# checking data types
"""
x= 32
print(type(x))

x=76.67
print(type(x))

x=[1,2,3,4,5,5,6]
print(type(x))

x=(1,2,3,4,5,5,6)
print(type(x))

x= person={
    "firstName":"Alex",
    "lastName":"Balor",
    "age":32,
    "gender":"Male",
    "isAmerican":True,
    "wealth":1318917489743424324324242,
    "color":"white",
    "height": "6 ft"

}

print(type(x))

"""


# Immutable Data checking
"""
x=12
print(id(x))
x=53
print(id(x))
x=3242
print(id(x))      #diffrent id numbers , different memory allocation 

"""

# Mutable Data checking
"""

countries = ["China","Russia","France"]
print(id(countries))


countries[0]= ["Poland"]
print(id(countries))                          #same id number, modified in place

"""



#Example of String data types
"""

name = 'Web are programming by "python"'  #single quote string
demo = "Web are programming by 'python'"  # double quote string

demo1 = '''
Web are programming by "python"
Python is a coding language
'''

demo2 ="""
Web are programming by 'python'       #shows error when quoted
Python is a coding language
"""

"""

#String positive indexing
"""
text = "hello world"
# 0 ->1 ->2 ->3 ->4 ->5 .................

print(text[1])
print(text[2])
print(text[3])
print(text[4])
"""

#String negative indexing
"""
text = "hello world"
#-1 -> -2 -> -3 -> -4 ->5 .......

print(text[-4])
print(text[-3])
print(text[-2])
print(text[-1])
"""

#String Slicing
"""
text = "Hello World"

print(len(text))
print(text[:7])     #string slicing syntax--> print(index[start range : end range ])
"""

#Sting concatenation
""" 
print("hello ", end="" ) + print("world",end="") 

string1="Hello"
string2="World"
                                        # (x) + " " -> {for a space} + (y)
combined = string1 + " " +  string2
print(combined)

"""

# string method(repetition)
"""
text = "Hello "
repeat = text*10
print(repeat)   
"""

#string method(Format using %)
"""
name = "Denis"  
age = 67
# %s = string placeholder
#%d =number placeholder

total = "My name is %s and my age is %d years old" % (name, age)
print(total)
"""

#string method(uppercase,lowercase,Capitalize,Title case)
"""
text = "hello world"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
"""

#string replacement
"""
text = "hello world"
new_text = text.replace("world", "hello")
print(new_text)
"""

#String split into list
"""
text = "hello world"
textlist = text.split()
print(textlist)
"""

#String tripping
"""
text = "                hello world         "
print(text.lstrip())
print(text.rstrip())
print(text.strip())
"""

#Python math(Factorial,Greatest Common Divisor,Lowest Common Divisor)
"""
import math


#Factorial
print("Factorial",math.factorial(19))

#Greatest Common Divisor
print("GCD",math.gcd(56,45,34))

#Lowest Common Divisor
print("LCM",math.lcm(54,56,75))
"""
marks = int(input("Enter marks: "))

if marks > 100 or marks < 0 :
    print ("wrong credentials, Enter number between 0 and 100")

elif 80 <= marks <= 100:
    print ("A+")

elif 70 <= marks <= 80:
    print ("A")

elif 60 <= marks <= 70:
    print ("A-")

elif 50 <= marks <= 60:
    print ("B+")

elif 40 <= marks <= 50:
    print ("B")


else :
    print ("F")


# Nested if / else

"""
age=34
permission = False

if age>=20:
     if permission == True:
         print("You can join the party")

     else:
         print("You can not join the party")

else:
    print("You are underaged")

"""

#Loop(for)

"""
cityList= ["Dhaka","Rajshahi","Rangpur","Barishal"]

#0 -> 1 -> 2 -> 3 -> 4 -> 5 ......

for city in  cityList:
    print(city)
    
"""

#Loop(While)


"""

countryList= ["Russia","UAE","China","Taiwan"]
index= 0
#0 -> 1 -> 2 -> 3 -> 4 -> 5 ......
while index<len(countryList):):
    print(countryList[index])
    index=index+1 
    
"""


"""
countryList= ["Russia","UAE","China","Taiwan"]

#0 -> 1 -> 2 -> 3 -> 4 -> 5 ......

for country in  countryList:
    if(country=="Russia"):
        continue                 #or break to stop loop

    print(country)


"""
#And
"""
age=87
permission = True


if age>=20 and permission == True:
    print("You can join with us")


"""
#Not
"""

age=10



if not age>=20 :
    print("You can join with us")
"""


# for loop with length of lists
"""
numbers = [3, 5, 6, 7]
for number in range (0,len(numbers)):
    print(numbers[number]) 
    """

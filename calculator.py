import math


print("Welcome to my basic calculator ,What do you want to do?")

def addition():
    num1 = float(input("What's x: "))
    num2 = float(input("What's y: "))
    print(f"{num1} plus {num2} is", float(num1) + float(num2))


def substraction():
    num1 = float(input("What's x: "))
    num2 = float(input("What's y: "))
    print(f"{num1} minus {num2} is", float(num1) - float(num2))


def multiplication():
    num1 = float(input("What's x: "))
    num2 = float(input("What's y: "))
    print(f"{num1} times {num2} is", float(num1) * float(num2))


def division():
    num1 = float(input("What's x: "))
    num2 = float(input("What's y: "))
    print(f"{num1} divided by {num2} is", float(num1) / float(num2))


def power():
    num1 = float(input("What's x: "))
    num2 = float(input("What's power: "))
    print(f"{num2} power of {num1} is", float(num1 ** num2))


def roots():
    num1 = float(input("What's x: "))
    num2 = float(input("What's y: "))
    print(f"{num2} root pf {num1} is", float(num1) // float(num2))


def trigonometric():
    print("What do you want to do next? "
          "\nPress 1 for sin0"
          "\nPress 2 for cos0"
          "\nPress 3 for tan0"
          "\nPress 4 for cot0"
          "\nPress 5 for sec0"
          "\nPress 6 for cosec0")

    tri_choice = int(input("Enter your choice: "))
    degrees = float(input("Enter your radians: "))

    if tri_choice == 1:
        print(f"The value of sin({degrees}) is", math.sin(math.radians(degrees)))

    elif tri_choice == 2:
        print(f"The value of cos({degrees}) is", math.cos(math.radians(degrees)))


    elif tri_choice == 3:

        if abs(math.cos(math.radians(degrees))) < 1e-10:

            print(f"Tan({degrees}) is undefined ")

        else:

            print(f"The value of tan({degrees}) is", math.tan(math.radians(degrees)))

    elif tri_choice == 4:
        print(f"The value of cot({degrees}) is", 1 / math.tan(math.radians(degrees)))

    elif tri_choice == 5:
        if abs(math.cos(math.radians(degrees))) < 1e-10:
            print(f"sec({degrees}) is undefined")

        else:
            print(f"The value of sec({degrees}) is", 1 / math.cos(math.radians(degrees)))

    elif tri_choice == 6:
        if abs(math.cos(math.radians(degrees))) < 1e-10:
            print(f"cosec({degrees}) is undefined")

        else:
            print(f"The value of cosec({degrees}) is", 1 / math.sin(math.radians(degrees)))


def logarithm():
    base = float(input("What's base: "))
    x = float(input("What's x: "))



    if base == 0 or x == 0:
        print("math error")
    else:
        print(f"{base} based log of {x} is", math.log(x, base))

while True:

    print("Press 1 for addition")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for power")
    print("Press 6 for roots")
    print("Press 7 for trigonometry")
    print("Press 8 for logarithm ")
    print("Press 0 to quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addition()
    elif choice == 2:
        substraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        power()
    elif choice == 6:
        roots()
    elif choice == 7:
        trigonometric()
    elif choice == 8:
        logarithm()
    elif choice == 0:
        print("Goodbye")
        break
    else :
        print("Invalid choice")

    print("\n\n--------------------------------\n\n")
























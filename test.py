def add (a,b):
    return a + b 

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b 

def calculator():
    print("select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input ("enter choice (1/2/3/4):")
    if choice in('1','2','3','4'):
        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Wrong input! please enter correct value")
            return
        if choice == 1:
            print(f"result: {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {subtract(num1, num2 )}")
        elif choice == 3:
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {divide(num1,num2)}")
            try:
                print(f"result: {divide(num1, num2)}")
            except ZeroDivisionError:
                print(f"numbers cannot be divide by zero")
    else:
        print("Choose a different operation!!")
        calculator()
        

        








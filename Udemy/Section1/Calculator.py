import math
import keyboard

class Calculatorclass():

    def _init_(self):
        print("Initialize")           

    def add(self, number1, number2):
        a=number1+number2
        return a

    def subtract(self, number1, number2):
        a=number1-number2
        return a
    
    def charan_test(self):       
        print("This is Charan's calculator")
        print("1. Operation")
        print("2. Shape")
        choice1 = input("Enter choice(1/2): ")
        print(choice1)

        if choice1 == "1":
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exponents")
            print("6. Square Toot")
            choice2 = input("Enter choice(1/2/3/4/5/6): ")

            if choice2 == "1":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                #print(num1,"+",num2,"=", add(num1,num2))
                print(num1+num2)

            elif choice2 == "2":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1-num2)

            elif choice2 == "3":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1*num2)

            elif choice2 == "4":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1/num2)

            elif choice2 == "5":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1**num2)

            elif choice2 == "6":
                num1 = float(input("Enter number: "))
                print(math.sqrt(num1))

            else:
                print("Invalid input")

        elif choice1 == "2":
            print("1. 2-D Shape")
            print("2. 3-D Shape")
            choice3 = input("Enter choice(1/2): ")

            if choice3 == "1":
                print("1. Triangle")
                print("2. Square")
                print("3. Pentagon")
                print("4. Hexagon")
                print("5. Heptagon")
                print("6. Octagon")
                print("7. Nonagon")
                print("8. Decagon")
                choice3 = input("Enter choice(1/2/3/4/5/6/7/8): ")

                if choice3 == "1":
                    num1 = float(input("Enter height: "))
                    num2 = float(input("Enter base: "))
                    print((num1*num2)/2)
                elif choice3 == "2":
                    num1 = float(input("Enter side length: "))
                    print(num1**22
                    )
        else:
            print("Invalid input")


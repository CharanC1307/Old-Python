import math
import keyboard
from mpmath import *

#problem with square root

print("This is Charan's calculator")
print("1. Operation")
print("2. Shape")
choice1 = input("Enter choice(1/2): ")

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
      num1 = (input("Enter first number: "))
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
      print("1. Area")
      print("2. Perimeter")
      choice4 = input("Enter choice(1/2): ")
      
      if choice4 == "1":
         print("1. Circle")
         print("2. Triangle")
         print("3. Square")
         print("4. Rectangle")
         print("5. Regular Pentagon")
         print("7. Regular Hexagon")
         print("8. Regular Heptagon")
         print("9. Regular Octagon")
         print("10. Regular Nonagon")
         print("11. Regular Decagon")
         choice5 = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
         #Circle
         if choice5 == "1":
            num1 = float(input("Enter Radius: "))
            print(math.pi*(num1**2))
         #Triangle
         elif choice5 == "2":
            print("1. Triangle")
            print("2. Regular Triangle")
            choice6 = input("Enter choice(1/2):")
            if choice6 == "1":
               print("1. Do you know height and base:")
               print("2. Do you know all the sides:")
               choice7 = input("Enter choice(1/2):")
               if choice7 == "1":
                  num1 = float(input("Enter height: "))
                  num2 = float(input("Enter base: "))
                  print((num1*num2)/2)
               elif choice7 == "2":
                  num1 = float(input("Enter side 1: "))
                  num2 = float(input("Enter side 2: "))
                  num3 = float(input("Enter side 3: "))
                  num4 = (1/2)*(num1+num2+num3)
                  print(math.sqrt((num4)*(num4-num1)*(num4-num2)*(num4-num3)))
            if choice6 == "2":
               num1 = float(input("Enter side length: "))
               print(((num1**2)/4)*math.sqrt(3))
         #square
         elif choice5 == "3":
            print("1. Do you know the side:")
            print("2. Do you know the diagonal:")
            choice6 = input("Enter choice(1/2):")
            if choice6 == "1":
               num1 = float(input("Enter side: "))
               print(num1**2)
            elif choice6 == "2":
               num1 = float(input("Enter diagonal: "))
               print((num1**2)/2)
         #Reactangle
         elif choice5 == "4":
            print("1. Do you know the side:")
            print("2. Do you know the diagonal and one side:")
            choice6 = input("Enter choice(1/2):")
            if choice6 == "1":
               num1 = float(input("Enter length: "))
               num2 = float(input("Enter width: "))
               print(num1*num2)
            elif choice6 == "2":
               num1 = float(input("Enter diagonal: "))
               num2 = float(input("Enter side: "))
               print(math.sqrt((num1**2)-(num2**2)))
         #Pentagon
         elif choice5 == "5":
            num1 = float(input("Enter side length: "))
            print((1/4)*(math.sqrt(5*(5+2*(math.sqrt(5)))))*(num1**2))
         elif choice5 == "7":
            num1 = float(input("Enter side length: "))
            print(((3*math.sqrt(3))/2)*(num1**2))
         elif choice5 == "8":
            num1 = float(input("Enter side length: "))
            print ((7/4)*(num1**2)*(cot(math.radians(180)/7)))
         elif choice5 == "9":
            num1 = float(input("Enter side length: "))
            print (2*(1+(math.sqrt(2)))*(num1**2))
         elif choice5 == "10":
            num1 = float(input("Enter side length: "))
            print ((9/4)*(num1**2)*(cot(math.radians(180)/9)))
         elif choice5 == "11":
            num1 = float(input("Enter side length: "))
            print ((5/2)*(num1**2)*(math.sqrt(5+2*(math.sqrt(5)))))
            

else:
   print("Invalid input")
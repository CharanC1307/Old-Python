import os
from Calculator import Calculatorclass

number1=int(input("Enter number 1 - "))
number2=int(input("Enter number 2 - "))
calc=Calculatorclass()
addition = calc.add(number1,number2)
print("Addition", str(addition))

subt = calc.subtract(number1,number2)
print("Substract", str(subt))
#addition = add(number1,number2)32

charan_t = calc.charan_test()
print("completed")



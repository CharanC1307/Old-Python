import pickle
import os

os.system("cls")

list=["Charan Chandran", "Sharvin Chandran", "Deepa Chithiravelu", "Chandran Muniyandi"]

print("Original List")
print(list)

pickle.dump(list, open("list", "wb"))

list.remove("Charan Chandran")

print("Changed List")
print(list)

list=pickle.load(open("list", "rb"))

print("Original List")
print(list)
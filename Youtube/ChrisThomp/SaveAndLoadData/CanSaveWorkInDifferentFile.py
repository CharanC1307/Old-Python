import pickle
import os

os.system("cls")

list=pickle.load(open("list", "rb"))

print("Original List")
print(list)
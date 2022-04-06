
from datetime import datetime
from time import gmtime, strftime

#result = time.strftime("%I:%M:%S %p", localtime)
currentDateTime=datetime.now().strftime('%Y-%m-%d %H-%M-%S')
fileName="TestFile_"+str(currentDateTime)+".txt"

filePath="C:\\Brothers\\Charan\\Python\\MyProjects\\Tkinter\\" + fileName

userName="Sharvin"
Password="Charan"

#W means - write
with open(filePath, 'a') as the_file:
    the_file.write(userName + ','+Password +'\n')

with open(filePath, 'r') as f:
    x = f.readlines()
    print(x)








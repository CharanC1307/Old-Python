import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CHARANPC\SQLEXPRESS;'
                      'Database=Student;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.students')

for row in cursor:
    if row.StudentID==1:
        
        print("Student 1  - ",row.FirstName, row.LastName )
    
    elif row.StudentID==2:
        print("Student 2 - ",row.FirstName, row.LastName )
    else:
        print("done")


    print("---------------------------------")
    print(row.StudentID,row.LastName)
    print("---------------------------------")
    print(row)

    print("---------------------------------")
    print(row[1])
import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CHARANPC\SQLEXPRESS;'
                      'Database=Student;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.students')

columns = [desc[0] for desc in cursor.description]
data = cursor.fetchall()
df = pd.DataFrame(list(data), columns=columns)


writer = pd.ExcelWriter('students.xlsx')
df.to_excel(writer, sheet_name='Student')
writer.save()
